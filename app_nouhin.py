import os
import sys
import calendar
from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from copy import copy

# PySide6（Qt）関連のインポート
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import loadUiType

# プロジェクト共通モジュールのインポート
import config
import common_utils

# UIファイルをプログラムとして直接ロード
ui_path = os.path.join(os.path.dirname(__file__), "app_nouhin.ui")
Ui_MainWindow, QMainWindowBase = loadUiType(ui_path)

class NouhinWindow(QMainWindowBase, Ui_MainWindow):
    """納品書に基づく売上内訳 ウィンドウ管理クラス"""

    def __init__(self, parent_menu=None):
        super().__init__()
        self.parent_menu = parent_menu
        self.init_ui()

    def init_ui(self):
        """UIの初期セットアップ（外観・シグナル接続）"""
        self.setupUi(self)

        # ウィンドウタイトルと共通アイコンの設定
        self.setWindowTitle("納品書に基づく売上内訳")
        common_utils.set_common_window_icon(self)

        # 初期値として現在のシステム日付（今日）をセット
        self.date_target_year_month.setDate(QDate.currentDate())

        # シグナル（イベント）の接続
        self.btn_back.clicked.connect(self.close_window)    # 戻るボタン
        self.btn_clear.clicked.connect(self.clear_ui)       # クリアボタン
        self.btn_exe_output.clicked.connect(self.run_query)     # 出力ボタン

    def clear_ui(self):
        """【クリアボタン押下時】入力を画面起動時の状態に戻す"""
        print("【ログ】画面上のデータをクリアします。")
        self.date_target_year_month.setDate(QDate.currentDate())

    def close_window(self):
        """【戻るボタン押下時】メニュー画面を再表示して自身を完全に閉じる"""
        print("【ログ】画面を閉じ、メニューを最前面に呼び出します。")
        if self.parent_menu:
            if hasattr(self.parent_menu, "deiconify"):
                self.parent_menu.deiconify()  # Tkinter用バックポインタ
            elif hasattr(self.parent_menu, "show_menu"):
                self.parent_menu.show_menu()  # PySide6(main.py)用バックポインタ
            elif hasattr(self.parent_menu, "show"):
                self.parent_menu.show()       # 通常のPySide6用バックポインタ
        self.close()

    def closeEvent(self, event):
        """【×ボタン押下時】戻るボタンと同じ終了処理をフックする"""
        self.close_window()
        event.accept()

    def run_query(self):
        """【出力ボタン押下時】条件を取得しSQLを実行、Excelに出力する"""
        q_date = self.date_target_year_month.date()
        year_val = q_date.year()
        month_val = q_date.month()
        start_date = f"{year_val:04d}-{month_val:02d}-01"
        _, last_day = calendar.monthrange(year_val, month_val)
        end_date = f"{year_val:04d}-{month_val:02d}-{last_day:02d}"
        
        sheet_name = f"{year_val:04d}年{month_val:02d}月"
        desktop_path = os.path.expanduser("~/Desktop")
        file_name = f"納品書に基づく売上内訳_{year_val}年{month_val}月.xlsx"
        save_path = os.path.join(desktop_path, file_name)

        try:
            query = """
                SELECT URH_DENDAT AS 日付
                ,SUM(CASE WHEN SHO_KBN = 3 AND URM_SHOCD NOT IN ('806000', '806005', '807000') THEN URM_URIKIN ELSE 0 END) AS 商品
                ,SUM(CASE WHEN URM_SHOCD = '806005' THEN URM_URIKIN ELSE 0 END) AS 荷造梱包費
                ,SUM(CASE WHEN URM_SHOCD = '807000' THEN URM_URIKIN ELSE 0 END) AS 雑収入
                ,SUM(CASE WHEN URM_SHOCD = '806000' THEN URM_URIKIN ELSE 0 END) AS 運賃
                ,SUM(CASE WHEN SHO_KBN = 2 THEN URM_URIKIN ELSE 0 END) AS 製品
                ,0 AS 売上合計
                ,SUM(CASE WHEN URM_SHOCD = '805000' THEN URM_SURYO ELSE 0 END) AS TPH_数量
                ,SUM(CASE WHEN URM_SHOCD = '805000' THEN URM_URIKIN ELSE 0 END) AS TPH_金額
                ,SUM(CASE WHEN URM_SHOCD = '804001' THEN URM_SURYO ELSE 0 END) AS 電纜_数量
                ,SUM(CASE WHEN URM_SHOCD = '804001' THEN URM_URIKIN ELSE 0 END) AS 電纜_金額
                FROM T_URHDAT
                INNER JOIN T_URMDAT ON URH_KCODE = URM_KCODE AND URH_DENNO = URM_DENNO
                LEFT JOIN T_SHOMST ON URM_SHOCD = SHO_SHOCD
                WHERE URH_DENDAT BETWEEN ? AND ?
                GROUP BY URH_DENDAT
                ORDER BY URH_DENDAT
            """
            conn = common_utils.get_db_connection()
            df = pd.read_sql(query, conn, params=[str(start_date), str(end_date)])
            conn.close()

            if df.empty:
                QMessageBox.information(self, "結果", "該当するデータは見つかりませんでした。")
                return

            # 元の動作通り、2行目（startrow=1）からPandasデータを出力
            with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name=sheet_name, startrow=1)

            wb = load_workbook(save_path)
            ws = wb.active
            s = common_utils.get_excel_styles()
            center_align = Alignment(horizontal='center', vertical='center', wrap_text=True)

            # 元の通り、2段目のヘッダー文字列を個別にセット
            ws['H2'] = "数量"
            ws['I2'] = "金額"
            ws['J2'] = "数量"
            ws['K2'] = "金額"

            # 🛠️ 【修正点①】結合する「前」に、全列のループ処理をして書式・罫線・数式を適用する
            for i, col in enumerate(ws.iter_cols(min_row=1, max_col=ws.max_column), 1):
                col_letter = get_column_letter(i)
                for cell in col:
                    cell.border = s["border"]
                    
                    # 1〜2行目（ヘッダー行）の装飾
                    if cell.row <= 2:
                        cell.fill = s["fill_header"]
                        cell.alignment = center_align
                        if cell.coordinate == "D1":
                            small_font = copy(s["font_bold"])
                            small_font.sz = 9
                            cell.font = small_font
                        else:
                            cell.font = s["font_bold"]
                    else:
                        # 明細行のフォント設定
                        cell.font = s["font"]

                    # 3行目以降（データ行）の数値フォーマットと数式
                    if cell.row >= 3:
                        if i == 1:
                            cell.number_format = 'm"月"d"日"'
                        elif i >= 2:
                            cell.number_format = '#,##0'

                        if i == 7:
                            cell.value = f"=SUM(B{cell.row}:F{cell.row})"

                # 🛠️ 【修正点②】列幅タイポの修復（元の条件に戻す）
                if i == 1:
                    ws.column_dimensions[col_letter].width = 10
                elif i == 3 or i == 5:
                    ws.column_dimensions[col_letter].width = 8
                elif i == 8 or i == 10:
                    ws.column_dimensions[col_letter].width = 10
                else:
                    ws.column_dimensions[col_letter].width = 15

            # 🛠️ 【修正点③】すべての値を配置し終わった「最後」に、セルを結合する（元の正常な順序）
            header_map = [
                ('A1:A2', '日付'), ('B1:B2', '商品売上'),
                ('C1:C2', '荷造梱包費'), ('D1:D2', '雑収入\n（梱包破損補償等）'),
                ('E1:E2', '運賃'), ('F1:F2', '製品'), ('G1:G2', '売上合計'),
                ('H1:I1', 'TPH8512RED'), ('J1:K1', '電纜ホース')
            ]
            for cell_range, title in header_map:
                ws.merge_cells(cell_range)
                # 結合の左上セルにタイトルを設定
                for row in ws[cell_range]:
                    top_left_cell = row[0]
                    top_left_cell.value = title
                    break

            # 最終行（合計行）の追加と装飾
            last_row = ws.max_row + 1
            ws.cell(row=last_row, column=1).value = "合計"
            for c in range(2, ws.max_column + 1):
                col_let = get_column_letter(c)
                target_cell = ws.cell(row=last_row, column=c)
                target_cell.value = f"=SUM({col_let}3:{col_let}{last_row-1})"
                target_cell.number_format = '#,##0'

            for c in range(1, ws.max_column + 1):
                cell = ws.cell(row=last_row, column=c)
                cell.border = s["border"]
                cell.fill = s["fill_total"]
                cell.font = s["font_bold"]

            ws.freeze_panes = 'A3'
            wb.save(save_path)
            QMessageBox.information(self, "完了", f"出力が完了しました。\n保存先: {save_path}")

        except PermissionError:
            QMessageBox.critical(self, "エラー", "Excelファイルが開いています。閉じてから再実行してください。")
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"処理中にエラーが発生しました:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NouhinWindow()
    window.show()
    sys.exit(app.exec())
