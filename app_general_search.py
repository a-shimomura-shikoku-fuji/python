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
    "と不一致 (!=)": "!=",
}


class GeneralSearchWindow(QMainWindowBase, Ui_MainWindow):
    """データベース汎用複数条件検索画面 ウィンドウ管理クラス"""

    def __init__(self, parent_menu=None):
        """初期化処理・コンポーネントとUIのセットアップ"""
        super().__init__()
        self.parent_menu = parent_menu
        self.current_df = None  # 検索結果データ保持
        self.table_columns = []  # 現在選択中のテーブル列名（物理IDリスト）
        self.conditions_pool = []  # 追加された条件の内部プール
        
        # 【日本語名称の自動管理用変数】
        self.header_mapping = {}  # { 物理ID: 日本語名 }
        self.col_name_to_id = {}  # { 日本語名: 物理ID } ◀ 条件逆変換用
        self.table_name_to_id = {}  # { テーブル表示名: 物理ID } ◀ テーブル逆変換用
        
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
            
            # 各テーブルの説明欄を自動取得してコンボボックスを構築
            target_tables = ["T_TOKMST","T_SHIMST","T_NOUMST", "T_SHOMST"]
            display_tables = []
            self.table_name_to_id.clear()
            
            conn = common_utils.get_db_connection()
            try:
                for t_id in target_tables:
                    # テーブル自体の説明欄(minor_id=0)を取得するクエリ
                    t_desc_query = """
                        SELECT CAST(ep.value AS NVARCHAR)
                        FROM sys.tables t
                        INNER JOIN sys.extended_properties ep 
                            ON ep.major_id = t.object_id 
                           AND ep.minor_id = 0 
                           AND ep.name = 'MS_Description'
                        WHERE t.name = ?
                    """
                    with conn.cursor() as cursor:
                        cursor.execute(t_desc_query, (t_id,))
                        row = cursor.fetchone()
                        # 💡【修正箇所】物理名を含めず、日本語説明のみを表示名として採用します
                        if row and row[0] and str(row[0]).strip():
                            t_name = str(row[0]).strip()
                        else:
                            t_name = t_id
                    
                    display_tables.append(t_name)
                    self.table_name_to_id[t_name] = t_id
            except Exception as e:
                print(f"テーブル日本語名の取得に失敗したため物理名を使用します: {e}")
                display_tables = target_tables
                self.table_name_to_id = {t: t for t in target_tables}
            finally:
                conn.close()

            self.cmb_table_name.addItems(display_tables)
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
        """選択テーブルからスキーマと日本語説明欄を一括抽出してコンボボックスを更新"""
        if not hasattr(self, "cmb_table_name") or not hasattr(self, "cmb_column_name"):
            return

        table_display = self.cmb_table_name.currentText().strip()
        if not table_display:
            return

        # 表示用の日本語名から、SQL用の物理テーブルID（T_URHDATなど）を逆引き
        table_name = self.table_name_to_id.get(table_display, table_display)

        self.cmb_column_name.clear()
        self.col_name_to_id.clear()
        
        conn = common_utils.get_db_connection()
        try:
            clean_table_name = "".join([c for c in table_name if c.isalnum() or c == "_"])
            
            # 1. 物理スキーマ（列名）を取得
            schema_query = f"SELECT TOP 1 * FROM {clean_table_name}"
            df_schema = pd.read_sql(schema_query, conn)
            self.table_columns = df_schema.columns.tolist()

            # 2. SQL Server拡張プロパティから日本語説明欄を一括取得
            local_map = {}
            desc_query = """
                SELECT c.name, CAST(ep.value AS NVARCHAR)
                FROM sys.tables t
                INNER JOIN sys.columns c ON t.object_id = c.object_id
                INNER JOIN sys.extended_properties ep 
                    ON ep.major_id = t.object_id 
                   AND ep.minor_id = c.column_id 
                   AND ep.name = 'MS_Description'
                WHERE t.name = ?
            """
            with conn.cursor() as cursor:
                cursor.execute(desc_query, (clean_table_name,))
                for col_id, col_name in cursor.fetchall():
                    if col_name and str(col_name).strip():
                        local_map[col_id] = str(col_name).strip()

            # 3. コンボボックス用表示アイテムの作成
            display_items = []
            for col in self.table_columns:
                if col in local_map:
                    jp_name = local_map[col]
                    display_items.append(jp_name)
                    self.col_name_to_id[jp_name] = col  # 日本語名から物理IDへの逆引き用
                else:
                    display_items.append(col)
                    self.col_name_to_id[col] = col

            self.cmb_column_name.addItems(display_items)

        except Exception as e:
            print(f"列スキーマ・日本語名のロードに失敗しました: {e}")
            self.table_columns = []
        finally:
            conn.close()

    def add_condition(self):
        """画面で組み立てられた日本語条件を内部リストに登録"""
        if not all(
            hasattr(self, attr)
            for attr in ["cmb_column_name", "cmb_operator", "text_cond_value", "listWidget_conds"]
        ):
            return

        col_display = self.cmb_column_name.currentText()
        op_display = self.cmb_operator.currentText()
        val = self.text_cond_value.toPlainText().strip()

        if not col_display or not val:
            QMessageBox.warning(self, "入力チェック", "列名と検索値を正しく入力・指定してください。")
            return

        # 表示されている日本語名から、対応する内部物理IDを安全に逆引き
        col_id = self.col_name_to_id.get(col_display, col_display)

        cond_item = {
            "column": col_id,  # 内部のSQLクエリ組み立てには物理IDを使用
            "op_type": OPERATORS[op_display],
            "value": val,
            "display": f"【{col_display}】 {op_display} '{val}'",  # 画面用リストには日本語で表示
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
        
        self.header_mapping.clear()
        self.col_name_to_id.clear()

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
            table_display = self.cmb_table_name.currentText().strip()
        else:
            return

        if not table_display:
            QMessageBox.warning(self, "入力エラー", "テーブル名を選択または入力してください。")
            return

        # 表示用の日本語名から、SQL用の物理テーブルID（T_URHDATなど）を逆引き
        table_name = self.table_name_to_id.get(table_display, table_display)

        conn = common_utils.get_db_connection()
        try:
            clean_table_name = "".join([c for c in table_name if c.isalnum() or c == "_"])
            query_string = f"SELECT TOP {MAX_ROWS} * FROM {clean_table_name}"
            where_clauses = []
            params = []

            for cond in self.conditions_pool:
                clean_col = "".join([c for c in cond["column"] if c.isalnum() or c == "_"])
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
                    mask = (
                        df.astype(str)
                        .apply(lambda row: row.str.contains(kw, case=False, na=False))
                        .any(axis=1)
                    )
                    df = df[mask]

                if df.empty:
                    QMessageBox.information(self, "結果", "キーワードに一致するデータは見つかりませんでした。")
                    self.clear_table_view()
                    return

            # 汎用整数型変換ガード
            for col in df.columns:
                non_na = df[col].dropna()
                if pd.api.types.is_numeric_dtype(df[col]) and not non_na.empty:
                    if (non_na % 1 == 0).all():
                        try:
                            df[col] = df[col].astype("Int64")
                        except Exception:
                            pass

            self.current_df = df

            # 【SQL Server拡張プロパティから日本語名（MS_Description）を一括ロード】
            self.header_mapping.clear()
            try:
                desc_query = """
                    SELECT c.name, CAST(ep.value AS NVARCHAR)
                    FROM sys.tables t
                    INNER JOIN sys.columns c ON t.object_id = c.object_id
                    INNER JOIN sys.extended_properties ep 
                        ON ep.major_id = t.object_id 
                       AND ep.minor_id = c.column_id 
                       AND ep.name = 'MS_Description'
                    WHERE t.name = ?
                """
                with conn.cursor() as cursor:
                    cursor.execute(desc_query, (clean_table_name,))
                    for col_id, col_name in cursor.fetchall():
                        if col_name and str(col_name).strip():
                            self.header_mapping[col_id] = str(col_name).strip()
            except Exception as e_desc:
                print(f"日本語名の取得中にスキップ（物理IDで表示します）: {e_desc}")

            # グリッドへ描画
            if hasattr(self, "tableWidget"):
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(len(df.columns))
                
                # 自動日本語優先ヘッターン適用
                headers = []
                for col in df.columns:
                    if col in self.header_mapping:
                        headers.append(self.header_mapping[col])
                    else:
                        headers.append(col)
                self.tableWidget.setHorizontalHeaderLabels(headers)

                for row_idx, row in df.iterrows():
                    self.tableWidget.insertRow(row_idx)
                    for col_idx, value in enumerate(row):
                        if pd.isna(value) or value is None:
                            item_text = ""
                        elif hasattr(value, "strftime"):
                            item_text = value.strftime("%Y-%m-%d %H:%M:%S")
                        else:
                            item_text = str(value)

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

        table_display = (
            self.cmb_table_name.currentText().strip()
            if hasattr(self, "cmb_table_name")
            else "汎用検索結果"
        )
        # 保存ファイル名用に日本語表示名から物理ID（T_URHDATなど）を逆引き
        table_name = self.table_name_to_id.get(table_display, table_display)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        desktop_path = os.path.expanduser("~/Desktop")
        file_name = f"{table_name}_{timestamp}.csv"
        save_path = os.path.join(desktop_path, file_name)

        try:
            self.current_df.to_csv(save_path, index=False, encoding="utf_sig")
            QMessageBox.information(self, "完了", f"CSV出力が完了しました。\n 保存先: {save_path}")
        except PermissionError:
            QMessageBox.critical(self, "エラー", "ファイルが開いています。閉じてから再実行してください。")
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"CSV出力中にエラーが発生しました:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeneralSearchWindow()
    window.show()
    sys.exit(app.exec())
