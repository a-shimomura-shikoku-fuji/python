import os
import sys
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import PatternFill

# PyQt6のインポート
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt, QDate

# 共通ユーティリティのインポート
import common_utils


class UrikakeWindow(QtWidgets.QMainWindow):
    """売掛金回収状況一覧 メイン画面クラス (app_urikake.ui 完全準拠)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_win = parent

        # 1. UIファイルの読み込み (絶対パスで固定)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(current_dir, "app_urikake.ui"), self)

        # 2. 画面位置・サイズの初期化 (UIの初期サイズ 436x286 に準拠)
        common_utils.center_window(self, 436, 286)

        # 3. 画面起動時の状態をセット (現在の年月)
        self.reset_to_initial_state()

        # 4. 使用しない空のボタンを非表示化 (誤操作防止)
        if hasattr(self, "pushButton_1"):
            self.pushButton_1.setVisible(False)
        if hasattr(self, "pushButton_3"):
            self.pushButton_3.setVisible(False)
        if hasattr(self, "pushButton_4"):
            self.pushButton_4.setVisible(False)

        # 5. UI上のオブジェクト名に基づいてイベント（シグナル）を接続
        self.btn_back.clicked.connect(self.on_closing)              # 戻るボタン
        self.btn_excel_2.clicked.connect(self.show_setting_window)  # 設定ボタン
        self.pushButton_10.clicked.connect(self.clear_fields)        # クリアボタン
        self.btn_excel.clicked.connect(self.run_query)              # 出力ボタン

    def reset_to_initial_state(self):
        """日付ボックスを画面起動時の状態（現在の年月）に戻す"""
        now = datetime.now()
        if hasattr(self, "date_Target"):
            self.date_Target.setDate(QDate(now.year, now.month, 1))

    def clear_fields(self):
        """クリアボタン (pushButton_10) 押下時：画面起動時の状態に戻す"""
        self.reset_to_initial_state()

    def on_closing(self):
        """戻るボタンまたは閉じる時の処理"""
        if self.parent_win:
            self.parent_win.show()  # メニュー画面を再表示
        self.close()

    def closeEvent(self, event):
        """×ボタン対策"""
        self.on_closing()
        event.accept()

    def run_query(self):
        """出力ボタン (btn_excel) 押下時のExcel出力メインロジック"""
        if hasattr(self, "date_Target"):
            qdate = self.date_Target.date()
            y_in = str(qdate.year())
            m_in = str(qdate.month())
        else:
            QtWidgets.QMessageBox.critical(self, "システムエラー", "日付ボックス(date_Target)が見つかりません。")
            return

        dt = common_utils.get_date_info(y_in, m_in)
        if not dt:
            QtWidgets.QMessageBox.warning(self, "入力エラー", "対象年月を正しく選択してください")
            return

        conn = common_utils.get_db_connection()
        cursor = conn.cursor()

        file_name = f"売掛金回収状況一覧_{dt['year']}年{dt['month']}月.xlsx"
        save_path = f"{dt['desktop_path']}/{file_name}"

        try:
            # --- 1. 新規得意先の同期処理 ---
            sync_query = """
            INSERT INTO Table_2 (code, sort, flag)
            SELECT TOK_TOKCD, 9999, 1
            FROM T_TOKMST
            WHERE NOT EXISTS (
                SELECT 1 FROM Table_2 WHERE Table_2.code = T_TOKMST.TOK_TOKCD
            )
            """
            cursor.execute(sync_query)
            conn.commit()

            # --- 2. メインのデータ抽出 ---
            query = """
            SELECT TOK_SIMEBI AS 締日
            ,CAST(code AS INT) AS コード
            ,TOK_TOKNM1 AS 得意先名
            ,NULL AS 区分
            ,ISNULL(SEK_URIAGE, 0) + ISNULL(SEK_TAX, 0) AS 売上金額
            ,NULL AS 入金額
            ,NULL AS 備考
            ,sort AS _sort_val
            FROM Table_2
            LEFT JOIN T_TOKMST ON code = TOK_TOKCD
            LEFT JOIN (
                SELECT SEK_SCODE, SEK_URIAGE, SEK_TAX, SES_SIMEDAT
                FROM T_SESDAT
                LEFT JOIN T_SEKDAT ON SES_KCODE = SEK_KCODE AND SES_SIMENO = SEK_SIMENO
                LEFT JOIN T_TOKMST ON SEK_KCODE = TOK_KCODE AND SEK_SCODE = TOK_TOKCD
                WHERE SES_SIMEDAT BETWEEN ? AND ?
            ) AS a ON code = SEK_SCODE
            WHERE (Table_2.flag = 1)
            OR (Table_2.flag = 0 AND (ISNULL(SEK_URIAGE, 0) + ISNULL(SEK_TAX, 0) <> 0))
            ORDER BY sort, code
            """
            df = pd.read_sql(query, conn, params=[dt["start"], dt["end"]])
            conn.close()

            if df.empty:
                QtWidgets.QMessageBox.information(self, "結果", "該当データはありませんでした。")
                return

            # --- 3. Excel装飾処理 ---
            with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name=dt["sheet_name"])

            wb = load_workbook(save_path)
            ws = wb.active
            s = common_utils.get_excel_styles()

            fill_new = PatternFill(fgColor="E2EFDA", fill_type="solid")
            sort_col_idx = ws.max_column

            for r_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=ws.max_row), 1):
                is_new = (ws.cell(row=r_idx, column=sort_col_idx).value == 9999)
                for c_idx, cell in enumerate(row, 1):
                    cell.border = s["border"]
                    cell.font = s["font"]
                    if r_idx == 1:
                        cell.fill = s["fill_header"]
                        cell.font = s["font_bold"]
                    elif is_new:
                        cell.fill = fill_new

                    if c_idx in and r_idx > 1:
                        cell.number_format = "#,##0"

            ws.delete_cols(sort_col_idx)

            # 列幅自動調整
            for i in range(1, ws.max_column + 1):
                col_letter = get_column_letter(i)
                max_len = 0
                for cell in ws[col_letter]:
                    if cell.value:
                        val_len = len(str(cell.value).encode("utf-16-le")) // 2
                        if val_len > max_len:
                            max_len = val_len
                if i in:
                    ws.column_dimensions[col_letter].width = 13.5
                else:
                    ws.column_dimensions[col_letter].width = (max_len + 4) * 1.2

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
                cell.border = s["border"]
                cell.fill = s["fill_total"]
                cell.font = s["font_bold"]

            wb.save(save_path)
            QtWidgets.QMessageBox.information(self, "完了", f"出力完了:\n{save_path}")

        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "エラー", "Excelを閉じてから実行してください。")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "エラー", f"失敗しました:\n{e}")

    def show_setting_window(self):
        """設定ボタン (btn_excel_2) 押下時の設定変更画面呼び出し"""
        self.setting_win = SettingWindow(self)
        self.setting_win.show()

class SettingWindow(QtWidgets.QDialog):
    """出力設定変更サブ画面 クラス (app_urikake_setting.ui 完全準拠)"""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent_win = parent

        # 1. UIファイルの読み込み (絶対パスで固定)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(current_dir, "app_urikake_setting.ui"), self)

        # 2. 画面位置・サイズの初期化 (UIの初期サイズ 436x286 に準拠)
        common_utils.center_window(self, 436, 286)

        # 3. QTextEditを1行のテキストボックスのように制御するための設定
        if hasattr(self, "text_tokcd"):
            self.text_tokcd.setFocus()
            self.text_tokcd.installEventFilter(self)  # Enter検知用のフィルター登録

        if hasattr(self, "text_sort"):
            self.text_sort.installEventFilter(self)  # Enter検知用のフィルター登録

        # 4. UI上のオブジェクト名に基づいてシグナルを接続
        self.btn_back.clicked.connect(self.close)              # 戻るボタン
        self.pushButton_10.clicked.connect(self.clear_fields)  # クリアボタン
        self.btn_excute.clicked.connect(self.update_settings)   # 変更ボタン

    def eventFilter(self, obj, event):
        """QTextEditでのEnterキー押下をフックするイベントフィルター"""
        if event.type() == event.Type.KeyPress:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                if obj == self.text_tokcd:
                    self.on_enter()
                    return True
                elif obj == self.text_sort:
                    self.update_settings()
                    return True
        return super().eventFilter(obj, event)

    def on_enter(self):
        """得意先コード入力後、Enterキーが押された時の検索処理"""
        raw_code = self.text_tokcd.toPlainText().strip()
        if not raw_code:
            return

        # ゼロ埋め処理 (8桁)
        code_8 = raw_code.zfill(8)
        self.text_tokcd.setPlainText(code_8)

        conn = common_utils.get_db_connection()
        query = """
        SELECT TOK_TOKNM1, sort, flag 
        FROM Table_2 
        LEFT JOIN T_TOKMST ON code = TOK_TOKCD 
        WHERE code = ?
        """
        res = conn.execute(query, (code_8,)).fetchone()
        conn.close()

        if res:
            cust_name = res if res else ""
            curr_sort = res
            curr_flag = res

            self.label_tokname.setText(cust_name)
            self.text_sort.setPlainText(str(curr_sort))
            self.chk_uriagezero.setChecked(True if curr_flag == 0 else False)

            self.text_sort.setFocus()
        else:
            QtWidgets.QMessageBox.warning(self, "未登録", "得意先が見つかりません。")

    def clear_fields(self):
        """クリアボタン (pushButton_10) 処理：画面起動時の状態（空欄）に戻す"""
        self.text_tokcd.clear()
        self.text_sort.clear()
        self.label_tokname.clear()
        self.chk_uriagezero.setChecked(False)
        self.text_tokcd.setFocus()

    def update_settings(self):
        """変更ボタン (btn_excute) 処理"""
        code = self.text_tokcd.toPlainText().strip()
        new_sort_input = self.text_sort.toPlainText().strip()

        if not code or not new_sort_input.isdigit():
            QtWidgets.QMessageBox.critical(self, "エラー", "入力内容を確認してください。")
            return

        new_sort = int(new_sort_input)
        new_flag = 0 if self.chk_uriagezero.isChecked() else 1

        conn = common_utils.get_db_connection()
        cursor = conn.cursor()

        try:
            # 最大値取得
            cursor.execute("SELECT ISNULL(MAX(sort), 0) FROM Table_2 WHERE sort < 9999")
            max_sort_res = cursor.fetchone()
            max_sort = max_sort_res if max_sort_res else 0

            if new_sort != 9999 and new_sort > max_sort:
                QtWidgets.QMessageBox.critical(
                    self, "入力エラー", f"表示順が大きすぎます。\n最大値は {max_sort} です。"
                )
                return

            cursor.execute("SELECT sort FROM Table_2 WHERE code = ?", (code,))
            old_sort_res = cursor.fetchone()
            if not old_sort_res:
                return
            old_sort = old_sort_res

            # 並び順の入れ替えロジック
            if old_sort != new_sort:
                if old_sort < 9999 and new_sort < 9999:
                    if old_sort < new_sort:
                        cursor.execute(
                            "UPDATE Table_2 SET sort = sort - 1 WHERE sort > ? AND sort <= ? AND sort < 9999",
                            (old_sort, new_sort),
                        )
                    else:
                        cursor.execute(
                            "UPDATE Table_2 SET sort = sort + 1 WHERE sort >= ? AND sort < ? AND sort < 9999",
                            (new_sort, old_sort),
                        )
                elif old_sort == 9999 and new_sort <= max_sort:
                    cursor.execute(
                        "UPDATE Table_2 SET sort = sort + 1 WHERE sort >= ? AND sort < 9999", (new_sort,)
                    )
                elif old_sort < 9999 and new_sort == 9999:
                    cursor.execute(
                        "UPDATE Table_2 SET sort = sort - 1 WHERE sort > ? AND sort < 9999", (old_sort,)
                    )

            cursor.execute(
                "UPDATE Table_2 SET sort = ?, flag = ? WHERE code = ?", (new_sort, new_flag, code)
            )
            conn.commit()

            QtWidgets.QMessageBox.information(self, "完了", f"得意先コード: {code}\n設定を更新しました。")
            self.on_enter()
            self.text_tokcd.setFocus()

        except Exception as e:
            conn.rollback()
            QtWidgets.QMessageBox.critical(self, "エラー", f"失敗しました: {e}")
        finally:
            conn.close()


# メニュー画面等から「別モジュールとして呼び出された時」の安全対策を施した起動ブロック
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UrikakeWindow()
    window.show()
    sys.exit(app.exec())
