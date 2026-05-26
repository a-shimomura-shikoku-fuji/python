import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime
import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import loadUiType

# 共通ユーティリティのインポート
import common_utils

# Pythonに古い一時ファイル（.pyc）を作らせない設定
sys.dont_write_bytecode = True

# UIファイルをロード
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
ui_main_path = os.path.join(root_dir, "ui_files", "app_general_search.ui")
Ui_MainWindow, QMainWindowBase = loadUiType(ui_main_path)

# --- 汎用検索画面の定数定義 ---
MAX_ROWS = 10000  # 最大取得件数制限

# 比較演算子のマッピング定義
OPERATORS = {
    "に一致する (=)": "=",
    "を含む (LIKE)": "LIKE",
    "で始まる": "START",
    "以上 (>=)": ">=",
    "以下 (<=)": "<=",
    "と不一致 (!=)": "!="
}


class GeneralSearchWindow(QMainWindowBase, Ui_MainWindow):
    """データベース汎用複数条件検索画面 ウィンドウ管理クラス"""

    def __init__(self, parent_menu=None):
        """初期化処理・コンポーネントとUIのセットアップ"""
        super().__init__()
        self.parent_menu = parent_menu
        self.current_df = None       # 検索結果データ保持
        self.table_columns = []      # 現在選択中のテーブル列名
        self.conditions_pool = []    # 追加された条件の内部プール
        self.init_ui()

    def init_ui(self):
        """UIの初期セットアップ（外観・シグナル接続）"""
        self.setupUi(self)
        self.setWindowTitle("データベース汎用複数条件検索")
        common_utils.set_common_window_icon(self)

        if hasattr(self, "cmb_operator"):
            self.cmb_operator.addItems(list(OPERATORS.keys()))

        if hasattr(self, "cmb_table_name"):
            self.cmb_table_name.setFocus()
            self.cmb_table_name.addItems(["T_URHDAT", "T_URMDAT", "T_SHOMST"])
            self.cmb_table_name.currentTextChanged.connect(self.on_table_changed)

        if hasattr(self, "btn_add_cond"):
            self.btn_add_cond.clicked.connect(self.add_condition)
        if hasattr(self, "btn_del_cond"):
            self.btn_del_cond.clicked.connect(self.delete_condition)

        if hasattr(self, "pushButton_ESC"):
            self.pushButton_ESC.clicked.connect(self.close_window)
        if hasattr(self, "pushButton_10"):
            self.pushButton_10.clicked.connect(self.clear_ui)
        if hasattr(self, "btn_exe_inquiry"):
            self.btn_exe_inquiry.clicked.connect(self.run_query)
        if hasattr(self, "btn_exe_csv"):
            self.btn_exe_csv.clicked.connect(self.export_csv)

        self.load_table_columns()

    def on_table_changed(self):
        """テーブル変更時の初期化ハンドラ"""
        self.conditions_pool.clear()
        if hasattr(self, "listWidget_conds"):
            self.listWidget_conds.clear()
        self.load_table_columns()

    def load_table_columns(self):
        """選択テーブルからスキーマ（列名）を自動抽出してコンボボックスを更新"""
        if not hasattr(self, "cmb_table_name") or not hasattr(self, "cmb_column_name"):
            return

        table_name = self.cmb_table_name.currentText().strip()
        if not table_name:
            return

        self.cmb_column_name.clear()
        conn = common_utils.get_db_connection()
        try:
            clean_table_name = "".join([c for c in table_name if c.isalnum() or c == '_'])
            schema_query = f"SELECT TOP 1 * FROM {clean_table_name}"
            df_schema = pd.read_sql(schema_query, conn)
            self.table_columns = df_schema.columns.tolist()
            self.cmb_column_name.addItems(self.table_columns)
        except Exception:
            self.table_columns = []
        finally:
            conn.close()

    def add_condition(self):
        """画面で組み立てられた条件を内部リストに登録"""
        if not all(hasattr(self, attr) for attr in ["cmb_column_name", "cmb_operator", "text_cond_value", "listWidget_conds"]):
            return

        col = self.cmb_column_name.currentText()
        op_display = self.cmb_operator.currentText()
        val = self.text_cond_value.toPlainText().strip()

        if not col or not val:
            QMessageBox.warning(self, "入力チェック", "列名と検索値を正しく入力・指定してください。")
            return

        cond_item = {
            "column": col,
            "op_type": OPERATORS[op_display],
            "value": val,
            "display": f"【{col}】 {op_display} '{val}'"
        }
        self.conditions_pool.append(cond_item)
        self.listWidget_conds.addItem(cond_item["display"])
        self.text_cond_value.clear()

    def delete_condition(self):
        """選択条件の削除処理"""
        if hasattr(self, "listWidget_conds"):
            current_row = self.listWidget_conds.currentRow()
            if current_row >= 0:
                self.listWidget_conds.takeItem(current_row)
                self.conditions_pool.pop(current_row)
    def clear_ui(self):
        """【クリアボタン押下時】完全リセット"""
        if hasattr(self, "cmb_table_name"):
            self.cmb_table_name.setCurrentIndex(0)
        if hasattr(self, "text_cond_value"):
            self.text_cond_value.clear()
        if hasattr(self, "text_keyword"):
            self.text_keyword.clear()
        if hasattr(self, "label_Count"):
            self.label_Count.clear()
        self.conditions_pool.clear()
        if hasattr(self, "listWidget_conds"):
            self.listWidget_conds.clear()
        self.clear_table_view()

    def clear_table_view(self):
        if hasattr(self, "tableWidget"):
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
        self.current_df = None

    def close_window(self):
        common_utils.handle_window_close(self, self.parent_menu)

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def run_query(self):
        """【照会ボタン押下時】複数条件をパラメタライズドクエリで結合・実行"""
        if hasattr(self, "cmb_table_name"):
            table_name = self.cmb_table_name.currentText().strip()
        else:
            return

        if not table_name:
            QMessageBox.warning(self, "入力エラー", "テーブル名を選択または入力してください。")
            return

        conn = common_utils.get_db_connection()
        try:
            clean_table_name = "".join([c for c in table_name if c.isalnum() or c == '_'])
            query_string = f"SELECT TOP {MAX_ROWS} * FROM {clean_table_name}"
            
            where_clauses = []
            params = []

            for cond in self.conditions_pool:
                clean_col = "".join([c for c in cond["column"] if c.isalnum() or c == '_'])
                op = cond["op_type"]
                val = cond["value"]

                if op == "LIKE":
                    where_clauses.append(f"{clean_col} LIKE ?")
                    params.append(f"%{val}%")
                elif op == "START":
                    where_clauses.append(f"{clean_col} LIKE ?")
                    params.append(f"{val}%")
                else:
                    where_clauses.append(f"{clean_col} {op} ?")
                    params.append(val)

            if where_clauses:
                query_string += " WHERE " + " AND ".join(where_clauses)
            
            if params:
                df = pd.read_sql(query_string, conn, params=params)
            else:
                df = pd.read_sql(query_string, conn)

            if df.empty:
                QMessageBox.information(self, "結果", "該当するデータは見つかりませんでした。")
                self.clear_table_view()
                return

            # 結果内横断キーワード絞り込み
            keyword_str = self.text_keyword.toPlainText().strip() if hasattr(self, "text_keyword") else ""
            if keyword_str:
                keywords = keyword_str.split()
                for kw in keywords:
                    mask = df.astype(str).apply(lambda row: row.str.contains(kw, case=False, na=False)).any(axis=1)
                    df = df[mask]

            if df.empty:
                QMessageBox.information(self, "結果", "キーワードに一致するデータは見つかりませんでした。")
                self.clear_table_view()
                return

            self.current_df = df

            # グリッドへ描画
            if hasattr(self, "tableWidget"):
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(len(df.columns))
                self.tableWidget.setHorizontalHeaderLabels(df.columns)

                for row_idx, row in df.iterrows():
                    self.tableWidget.insertRow(row_idx)
                    for col_idx, value in enumerate(row):
                        if isinstance(value, datetime):
                            item_text = value.strftime('%Y-%m-%d %H:%M:%S')
                        else:
                            item_text = str(value) if pd.notna(value) else ""
                        self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(item_text))

                self.tableWidget.resizeColumnsToContents()

            if hasattr(self, "label_Count"):
                self.label_Count.setText(f"表示件数: {len(df):,} 件")

        except Exception as e:
            QMessageBox.critical(self, "エラー", f"データ取得中にエラーが発生しました:\n{e}")
        finally:
            conn.close()

    def export_csv(self):
        """表示結果をデスクトップへCSV出力"""
        if self.current_df is None or self.current_df.empty:
            QMessageBox.warning(self, "出力エラー", "出力するデータがありません。先に照会を実行してください。")
            return

        table_name = self.cmb_table_name.currentText().strip() if hasattr(self, "cmb_table_name") else "汎用検索結果"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        desktop_path = os.path.expanduser("~/Desktop")
        file_name = f"{table_name}_{timestamp}.csv"
        save_path = os.path.join(desktop_path, file_name)

        try:
            self.current_df.to_csv(save_path, index=False, encoding="utf_sig")
            QMessageBox.information(self, "完了", f"CSV出力が完了しました。\n保存先: {save_path}")
        except PermissionError:
            QMessageBox.critical(self, "エラー", "ファイルが開いています。閉じてから再実行してください。")
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"CSV出力中にエラーが発生しました:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeneralSearchWindow()
    window.show()
    sys.exit(app.exec())