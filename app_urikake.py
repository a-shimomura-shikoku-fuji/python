import os
import sys
from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PySide6.QtUiTools import loadUiType

# 共通ユーティリティのインポート
import common_utils

# Pythonに古い一時ファイル（.pyc）を一切作らせない・読み込させない設定
sys.dont_write_bytecode = True

# メイン画面のUIファイルをロード
ui_main_path = os.path.join(os.path.dirname(__file__), "app_urikake.ui")
Ui_MainWindow, QMainWindowBase = loadUiType(ui_main_path)


class UrikakeWindow(QMainWindowBase, Ui_MainWindow):
    """売掛金回収状況一覧 メイン画面クラス"""

    def __init__(self, parent_menu=None):
        super().__init__()
        self.parent_menu = parent_menu
        self.setupUi(self)

        # 画面位置の初期化（PySide6標準の命令で安全に中央配置）
        self.resize(436, 286)
        screen_geo = self.screen().geometry()
        x = (screen_geo.width() - 436) // 2
        y = (screen_geo.height() - 286) // 2
        self.move(x, y)

        # 画面起動時の状態をセット (現在の年月)
        self.reset_to_initial_state()

        # ボタンのメンバ変数を初期化
        self.btn_back = None
        self.btn_setting = None
        self.pushButton_10 = None
        self.btn_excel = None

        # 画面全体のすべてのボタンを走査し、文字を基準に役割を固定
        all_buttons = self.findChildren(QPushButton)
        for btn in all_buttons:
            text = btn.text().strip()
            if text == "戻る":
                self.btn_back = btn
            elif text == "設定":
                self.btn_setting = btn
            elif text == "クリア":
                self.pushButton_10 = btn
            elif text == "出力":
                self.btn_excel = btn
            elif text == "":
                btn.setVisible(False)

        # 各ボタンのイベント（シグナル）接続
        if self.btn_back:
            self.btn_back.clicked.connect(self.close_window)
        if self.btn_setting:
            self.btn_setting.clicked.connect(self.show_setting_window)
        if self.pushButton_10:
            self.pushButton_10.clicked.connect(self.clear_fields)
        if self.btn_excel:
            self.btn_excel.clicked.connect(self.run_query)

    def reset_to_initial_state(self):
        """日付ボックスを画面起動時の状態（現在の年月）に戻す"""
        now = datetime.now()
        if hasattr(self, "date_Target"):
            self.date_Target.setDate(QDate(now.year, now.month, 1))

    def clear_fields(self):
        """クリアボタン 押下時：画面起動時の状態に戻す"""
        self.reset_to_initial_state()

    def close_window(self):
        """メニュー画面を再表示して自身を完全に閉じる"""
        if self.parent_menu and hasattr(self.parent_menu, "show"):
            self.parent_menu.show()
        self.close()

    def closeEvent(self, event):
        """×ボタン対策"""
        self.close_window()
        event.accept()

    def show_setting_window(self):
        """設定変更サブ画面の呼び出し"""
        self.setting_win = SettingWindow(self)
        self.setting_win.show()

    def run_query(self):
        """出力ボタン (btn_excel) 押下時のExcel出力メインロジック"""
        if hasattr(self, "date_Target"):
            qdate = self.date_Target.date()
            y_in = str(qdate.year())
            m_in = str(qdate.month())
        else:
            QMessageBox.critical(self, "システムエラー", "日付ボックス(date_Target)が見つかりません。")
            return

        dt = common_utils.get_date_info(y_in, m_in)
        if not dt:
            QMessageBox.warning(self, "入力エラー", "対象年月を正しく選択してください")
            return

        conn = common_utils.get_db_connection()
        cursor = conn.cursor()
        file_name = f"売掛金回収状況一覧_{dt['year']}年{dt['month']}月.xlsx"
        save_path = f"{dt['desktop_path']}/{file_name}"

        try:
            # --- 1. 新規得意先の同期処理 ---
            sync_query = """
                INSERT INTO Table_2 (code, sort, flag)
                SELECT TOK_TOKCD, 9999, 1 FROM T_TOKMST
                WHERE NOT EXISTS (SELECT 1 FROM Table_2 WHERE Table_2.code = T_TOKMST.TOK_TOKCD)
            """
            cursor.execute(sync_query)
            conn.commit()

            # --- 2. メインのデータ抽出 ---
            query = """
                SELECT TOK_SIMEBI AS 締日, CAST(code AS INT) AS コード, TOK_TOKNM1 AS 得意先名,
                       NULL AS 区分, ISNULL(SEK_URIAGE, 0) + ISNULL(SEK_TAX, 0) AS 売上金額,
                       NULL AS 入金額, NULL AS 備考, sort AS _sort_val
                FROM Table_2
                LEFT JOIN T_TOKMST ON code = TOK_TOKCD
                LEFT JOIN (
                    SELECT SEK_SCODE, SEK_URIAGE, SEK_TAX, SES_SIMEDAT FROM T_SESDAT
                    LEFT JOIN T_SEKDAT ON SES_KCODE = SEK_KCODE AND SES_SIMENO = SEK_SIMENO
                    LEFT JOIN T_TOKMST ON SEK_KCODE = TOK_KCODE AND SEK_SCODE = TOK_TOKCD
                    WHERE SES_SIMEDAT BETWEEN ? AND ?
                ) AS a ON code = SEK_SCODE
                WHERE (Table_2.flag = 1) OR (Table_2.flag = 0 AND (ISNULL(SEK_URIAGE, 0) + ISNULL(SEK_TAX, 0) <> 0))
                ORDER BY sort, code
            """
            df = pd.read_sql(query, conn, params=(dt["start"], dt["end"]))
            conn.close()

            if df.empty:
                QMessageBox.information(self, "結果", "該当データはありませんでした。")
                return

            # Excel書き込み
            with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name=dt["sheet_name"])

            wb = load_workbook(save_path)
            ws = wb.active

            side_thin = Side(border_style="thin", color="000000")
            border_all = Border(left=side_thin, right=side_thin, top=side_thin, bottom=side_thin)
            font_normal = Font(name="MS Gothic", size=11, bold=False)
            font_bold = Font(name="MS Gothic", size=11, bold=True)
            fill_header = PatternFill(fgColor="D9E1F2", fill_type="solid")
            fill_total = PatternFill(fgColor="F2F2F2", fill_type="solid")
            fill_new = PatternFill(fgColor="E2EFDA", fill_type="solid")

            sort_col_idx = ws.max_column

            # セル書式・スタイルの適用
            for r_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=ws.max_row), 1):
                is_new = (ws.cell(row=r_idx, column=sort_col_idx).value == 9999)
                for c_idx, cell in enumerate(row, 1):
                    cell.border = border_all
                    cell.font = font_normal
                    if r_idx == 1:
                        cell.fill = fill_header
                        cell.font = font_bold
                    elif is_new:
                        cell.fill = fill_new
                    
                    # 金額・コード列の3桁カンマ区切り（2列目と5列目）
                    if c_idx in [2, 5] and r_idx > 1:
                        cell.number_format = "#,##0"

            # ソート用の一時列を削除
            ws.delete_cols(sort_col_idx)

            # 列幅の自動調整（不必要なエンコード計算を最適化）
            for i in range(1, ws.max_column + 1):
                col_letter = get_column_letter(i)
                if i in [2, 5]:
                    ws.column_dimensions[col_letter].width = 13.5
                else:
                    max_len = max((len(str(cell.value or '')) for cell in ws[col_letter]), default=0)
                    ws.column_dimensions[col_letter].width = max(max_len + 4, 10) * 1.2

            # データ入力規則 (D列: 区分)
            dv = DataValidation(type="list", formula1='"でんさい,振込,相殺"', allow_blank=True)
            dv.add(f"D2:D{ws.max_row}")
            ws.add_data_validation(dv)
            ws.freeze_panes = "A2"

            # 合計行の追加
            last_row = ws.max_row + 1
            ws.cell(row=last_row, column=3).value = "合計"
            sum_col = get_column_letter(5)
            ws.cell(row=last_row, column=5).value = f"=SUM({sum_col}2:{sum_col}{last_row-1})"
            ws.cell(row=last_row, column=5).number_format = "#,##0"

            for c in range(1, 8):
                cell = ws.cell(row=last_row, column=c)
                cell.border = border_all
                cell.fill = fill_total
                cell.font = font_bold

            wb.save(save_path)
            QMessageBox.information(self, "完了", f"出力完了:\n{save_path}")

        except PermissionError:
            QMessageBox.critical(self, "エラー", "Excelを閉じてから実行してください。")
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"失敗しました:\n{e}")

# 設定画面のUIファイルをロード（重複していた箇所の集約）
ui_sub_path = os.path.join(os.path.dirname(__file__), "app_urikake_setting.ui")
Ui_SettingDialog, _ = loadUiType(ui_sub_path)


class SettingWindow(QMainWindow, Ui_SettingDialog):
    """出力設定変更サブ画面 クラス"""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent_win = parent
        self.setupUi(self)

        # 画面位置の初期化
        self.resize(436, 286)
        screen_geo = self.screen().geometry()
        x = (screen_geo.width() - 436) // 2
        y = (screen_geo.height() - 286) // 2
        self.move(x, y)

        # 子画面として最前面に固定
        self.setWindowModality(Qt.WindowModality.WindowModal)

        # Tabキーフォーカス設定
        if hasattr(self, "chk_uriagezero"):
            self.chk_uriagezero.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        # 初期フォーカスとリアルタイム変更監視のシグナル接続
        if hasattr(self, "text_tokcd"):
            self.text_tokcd.setFocus()
            self.text_tokcd.textChanged.connect(self.handle_tokcd_change)
        if hasattr(self, "text_sort"):
            self.text_sort.textChanged.connect(self.handle_sort_change)

        # ボタン類のシグナル接続
        self.btn_back.clicked.connect(self.close)
        self.pushButton_10.clicked.connect(self.clear_fields)
        self.btn_excute.clicked.connect(self.update_settings)

    def handle_tokcd_change(self):
        """得意先コード欄でEnterやTabが入力された瞬間に自動検索して、表示順へ移動する処理"""
        if not hasattr(self, "text_tokcd"):
            return
        txt = self.text_tokcd.toPlainText()

        if "\n" in txt or "\t" in txt:
            self.on_enter()
            if hasattr(self.text_tokcd, "textCursor"):
                cursor = self.text_tokcd.textCursor()
                cursor.movePosition(cursor.MoveOperation.End)
                self.text_tokcd.setTextCursor(cursor)
                self.text_tokcd.ensureCursorVisible()

            if hasattr(self, "text_sort"):
                self.text_sort.setFocus()
                if hasattr(self.text_sort, "selectAll"):
                    self.text_sort.selectAll()

    def handle_sort_change(self):
        """表示順欄での改行(Enter)を検知して、自動で「変更（更新）」を実行する処理"""
        if not hasattr(self, "text_sort"):
            return
        txt = self.text_sort.toPlainText()
        if "\n" in txt:
            self.text_sort.blockSignals(True)
            self.text_sort.setPlainText("". join(filter(str.isdigit, txt)))
            self.text_sort.blockSignals(False)
            self.update_settings()

    def on_enter(self):
        """得意先コード入力後の検索・ゼロ埋めと画面表示処理"""
        raw_code = self.text_tokcd.toPlainText().strip()
        if not raw_code:
            return

        code_8 = "".join(filter(str.isdigit, raw_code)).zfill(8)

        self.text_tokcd.blockSignals(True)
        self.text_tokcd.setPlainText(code_8)
        self.text_tokcd.blockSignals(False)

        conn = common_utils.get_db_connection()
        query = "SELECT TOK_TOKNM1, sort, flag FROM Table_2 LEFT JOIN T_TOKMST ON code = TOK_TOKCD WHERE code = ?"
        res = conn.execute(query, (code_8,)).fetchone()
        conn.close()

        if res:
            cust_name = res[0] if res[0] else ""
            curr_sort = res[1] if res[1] is not None else ""
            curr_flag = res[2]

            self.label_tokname.setText(cust_name)

            if hasattr(self, "text_sort"):
                self.text_sort.blockSignals(True)
                self.text_sort.setPlainText(str(curr_sort))
                self.text_sort.ensureCursorVisible()
                self.text_sort.blockSignals(False)

            self.chk_uriagezero.setChecked(True if curr_flag == 0 else False)
        else:
            QMessageBox.warning(self, "未登録", "得意先が見つかりません。")

    def clear_fields(self):
        """クリアボタン (pushButton_10) 処理"""
        if hasattr(self, "text_tokcd"):
            self.text_tokcd.blockSignals(True)
            self.text_tokcd.clear()
            self.text_tokcd.blockSignals(False)

        if hasattr(self, "text_sort"):
            self.text_sort.blockSignals(True)
            self.text_sort.clear()
            self.text_sort.blockSignals(False)

        self.label_tokname.setText("")
        self.chk_uriagezero.setChecked(False)
        self.text_tokcd.setFocus()

    def update_settings(self):
        """変更ボタン (btn_excute) 処理"""
        code = self.text_tokcd.toPlainText().strip()
        new_sort_input = self.text_sort.toPlainText().strip()

        code = "".join(filter(str.isdigit, code))
        new_sort_input = "".join(filter(str.isdigit, new_sort_input))

        if not code or not new_sort_input.isdigit():
            QMessageBox.critical(self, "エラー", "入力内容を確認してください。")
            return

        new_sort = int(new_sort_input)
        new_flag = 0 if self.chk_uriagezero.isChecked() else 1

        conn = common_utils.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ISNULL(MAX(sort), 0) FROM Table_2 WHERE sort < 9999")
            max_sort_res = cursor.fetchone()
            max_sort = max_sort_res[0] if max_sort_res else 0

            if new_sort != 9999 and new_sort > max_sort:
                QMessageBox.critical(self, "入力エラー", f"表示順が大きすぎます。\n最大値は {max_sort} です。")
                return

            cursor.execute("SELECT sort FROM Table_2 WHERE code = ?", (code,))
            old_sort_res = cursor.fetchone()
            if not old_sort_res:
                return
            old_sort = old_sort_res[0]

            if old_sort != new_sort:
                if old_sort < 9999 and new_sort < 9999:
                    if old_sort < new_sort:
                        cursor.execute("UPDATE Table_2 SET sort = sort - 1 WHERE sort > ? AND sort <= ? AND sort < 9999", (old_sort, new_sort))
                    else:
                        cursor.execute("UPDATE Table_2 SET sort = sort + 1 WHERE sort >= ? AND sort < ? AND sort < 9999", (new_sort, old_sort))
                elif old_sort == 9999 and new_sort <= max_sort:
                    cursor.execute("UPDATE Table_2 SET sort = sort + 1 WHERE sort >= ? AND sort < 9999", (new_sort,))
                elif old_sort < 9999 and new_sort == 9999:
                    cursor.execute("UPDATE Table_2 SET sort = sort - 1 WHERE sort > ? AND sort < 9999", (old_sort,))

            cursor.execute("UPDATE Table_2 SET sort = ?, flag = ? WHERE code = ?", (new_sort, new_flag, code))
            conn.commit()
            QMessageBox.information(self, "完了", f"得意先コード: {code}\n設定を更新しました。")
            self.on_enter()
            self.text_tokcd.setFocus()
        except Exception as e:
            conn.rollback()
            QMessageBox.critical(self, "エラー", f"失敗しました: {e}")
        finally:
            conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UrikakeWindow()
    window.show()
    sys.exit(app.exec())
