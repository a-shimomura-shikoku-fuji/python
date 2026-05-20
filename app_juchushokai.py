import os
import sys
import pandas as pd
import common_utils

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QBrush, QColor, QFont, QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QMessageBox,
)

class MyWindow(QMainWindow):

    def __init__(self, parent_root=None):
        super().__init__()
        self.parent_root = parent_root

        # --- 伝票めくり機能用の変数 ---
        self.current_group_idx = -1  # 現在表示しているグループのインデックス
        self.grouped_keys = []  # グループ化されたキーのリスト
        self.all_details_df = None  # 全明細データを保持するDataFrame
        
        # 1. UIファイルのパス設定と読み込み
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "app_juchushokai.ui")
        loader = QUiLoader()
        loaded_ui = loader.load(ui_path)

        # 2. メイン画面の構築とUI構造の移植
        self.setCentralWidget(loaded_ui.centralWidget())

        # 【★この1行を追加】UIファイルに設定されたスタイルシート（色など）をウィンドウ全体に適用する
        self.setStyleSheet(loaded_ui.styleSheet())

        if hasattr(loaded_ui, "menuBar") and loaded_ui.menuBar():
            self.setMenuBar(loaded_ui.menuBar())
        if hasattr(loaded_ui, "statusBar") and loaded_ui.statusBar():
            self.setStatusBar(loaded_ui.statusBar())

        # 3. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.resize(loaded_ui.size())
        self.setWindowTitle(loaded_ui.windowTitle())
        self.setWindowIcon(QIcon("my_logo.ico"))

        # 4. UIオブジェクトの保持とイベント連携
        self.ui = loaded_ui

        # pushButton_2 (前へ) のイベント連携（重複切断つき）
        if hasattr(self.ui, "pushButton_2"):
            try:
                self.ui.pushButton_2.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_2.clicked.connect(self.on_prevButton_click)

        # pushButton_3 (次へ) のイベント連携（重複切断つき）
        if hasattr(self.ui, "pushButton_3"):
            try:
                self.ui.pushButton_3.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_3.clicked.connect(self.on_nextButton_click)

         # 画面起動時に日付を設定する
        self.init_ui()

        # 5. テーブル（表）の初期化とデザイン適用
        self.init_table_design()

        # 6. 画面起動時に自動でデータをロードする
        self.load_initial_data()

    def init_ui(self):
        date_Nouki_F = self.ui.date_Nouki_F
        date_Nouki_T = self.ui.date_Nouki_T
        date_Dendat_F = self.ui.date_Dendat_F
        date_Dendat_T = self.ui.date_Dendat_T

        date_Nouki_F.setDate(QDate.currentDate())
        date_Nouki_T.setDate(QDate.currentDate())
        date_Dendat_F.setDate(QDate.currentDate().addYears(-1))
        date_Dendat_T.setDate(QDate.currentDate().addDays(-1))

    def init_table_design(self):
        """テーブル（表）の初期デザインを設定する"""
        if not hasattr(self, "ui") or not hasattr(self.ui, "tableWidget"):
            print("【警告】UI上の tableWidget が見つかりません。")
            return

        table = self.ui.tableWidget

        # --- テーブルのデザイン初期化処理 ---
        table.setColumnCount(4)

        headers = [
            "受注番号",
            "商品名 / サイズ",
            "数量明細 / 客先仕様No",
            "単価 / 備考",
        ]
        table.setHorizontalHeaderLabels(headers)

        table.setColumnWidth(0, 100)
        table.setColumnWidth(1, 180)
        table.setColumnWidth(2, 200)
        table.setColumnWidth(3, 130)

        if hasattr(table, "verticalHeader"):
            table.verticalHeader().setVisible(False)

        print("【ログ】テーブルのデザイン適用が完了しました。")

    def load_initial_data(self):
        """画面起動時にDBから全件取得して最初の1件目を表示する"""
        print("【ログ】初期データの読み込みを開始します。")
        
        # 1. プレースホルダを「:名前」から「?」に変更する
        sql = """
        SELECT
            JUH_DENDAT,
            JUH_JUHNO,
            JUM_TYUBAN,
            JUH_NOUKI,
            JUH_TOKNM1,
            JUH_TANCD,
            TAN_NAME,
            JUM_SHONM,
            JUM_KIKAKU,
            JUM_SURYOMEI,
            JUM_CUSTSYNO,
            JUM_URITAN,
            JUM_BIKOU1
        FROM T_JUHDAT
        INNER JOIN T_JUMDAT 
            ON JUH_KCODE = JUM_KCODE
            AND JUH_DENNO = JUM_DENNO
        LEFT OUTER JOIN T_TANMST
            ON JUH_TANCD = TAN_CODE
        WHERE JUH_NOUKI BETWEEN ? AND ?
        AND JUH_DENDAT BETWEEN ? AND ?    
        ORDER BY JUH_DENDAT, JUM_TYUBAN, JUH_NOUKI, JUH_TOKNM1, JUH_TANCD
        """

        # 2. 辞書型「{}」ではなく、リスト型「[]」でSQLに出現する順番通りに並べる
        sql_params = [
            self.ui.date_Nouki_F.date().toString("yyyy-MM-dd"),   # 1つ目の「?」
            self.ui.date_Nouki_T.date().toString("yyyy-MM-dd"),   # 2つ目の「?」
            self.ui.date_Dendat_F.date().toString("yyyy-MM-dd"),  # 3つ目の「?」
            self.ui.date_Dendat_T.date().toString("yyyy-MM-dd")   # 4つ目の「?」
        ]

        try:
            conn = common_utils.get_db_connection()
            
            # 3. params 引数にリストを渡してSQLを実行
            self.all_details_df = pd.read_sql(sql, conn, params=sql_params)
            conn.close()

            if self.all_details_df.empty:
                QMessageBox.information(
                    self, "確認", "該当するデータは見つかりませんでした。"
                )
                self.all_details_df = None
                return

            group_keys = [
                "JUH_DENDAT",
                "JUM_TYUBAN",
                "JUH_NOUKI",
                "JUH_TOKNM1",
                "JUH_TANCD",
            ]
            self.grouped_keys = list(
                self.all_details_df[group_keys]
                .drop_duplicates()
                .itertuples(index=False, name=None)
            )

            # 最初は必ず 0 (1件目)
            self.current_group_idx = 0

            print(
                f"【ログ】全明細を取得しました。件数: {len(self.all_details_df)} / グループ数: {len(self.grouped_keys)}"
            )

            self._display_current_group()

        except Exception as e:
            QMessageBox.critical(
                self,
                "エラー",
                f"データベース処理中にエラーが発生しました:\n{str(e)}",
            )
            self.all_details_df = None

    def on_nextButton_click(self):
        """pushButton_2（次へ）がクリックされた際、インデックスを1つ進めて表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        # インデックスを1つ進める
        self.current_group_idx += 1

        # 最後のデータを超えたら、最初のデータ(0)に戻る
        if self.current_group_idx >= len(self.grouped_keys):
            QMessageBox.information(
                self, "確認", "最後のデータです。最初のデータに戻ります。"
            )
            self.current_group_idx = 0
        elif self.current_group_idx == len(self.grouped_keys) - 1 and self.ui.pushButton_2.clicked:
            # 2回目の押下の場合は最後のデータに遷移する
            self.current_group_idx = 0
            QMessageBox.information(
                self, "確認", "最後のデータです。最初のデータに戻ります。"
            )

        self._display_current_group()

    def on_prevButton_click(self):
        """pushButton_3（前へ）がクリックされた際、インデックスを1つ戻して表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        # インデックスを1つ戻す
        self.current_group_idx -= 1

        # 最初のデータ(0)を下回ったら、最後のデータに移動する
        if self.current_group_idx < 0:
            QMessageBox.information(
                self, "確認", "最初のデータです。最後のデータに移動します。"
            )
            self.current_group_idx = len(self.grouped_keys) - 1

        self._display_current_group()

    def _display_current_group(self):
        """保持しているデータから、現在のインデックスのグループ・明細を表示する内部関数"""
        if not self.grouped_keys or self.all_details_df is None:
            return

        current_key = self.grouped_keys[self.current_group_idx]
        key_dendat, key_tyuban, key_nouki, key_toknm1, key_tancd = current_key

        df_sub = self.all_details_df[
            (
                (self.all_details_df["JUH_DENDAT"] == key_dendat)

                | (
                    pd.isna(self.all_details_df["JUH_DENDAT"])
                    & pd.isna(key_dendat)
                )
            )
            & (
                (self.all_details_df["JUM_TYUBAN"] == key_tyuban)
                | (
                    pd.isna(self.all_details_df["JUM_TYUBAN"])
                    & pd.isna(key_tyuban)
                )
            )
            & (
                (self.all_details_df["JUH_NOUKI"] == key_nouki)

                | (
                    pd.isna(self.all_details_df["JUH_NOUKI"])
                    & pd.isna(key_nouki)
                )
            )
            & (
                (self.all_details_df["JUH_TOKNM1"] == key_toknm1)
                | (
                    pd.isna(self.all_details_df["JUH_TOKNM1"])
                    & pd.isna(key_toknm1)
                )
            )
            & (
                (self.all_details_df["JUH_TANCD"] == key_tancd)

                | (
                    pd.isna(self.all_details_df["JUH_TANCD"])
                    & pd.isna(key_tancd)
                )
            )
        ]

        first_row = df_sub.iloc[0].to_dict()

        def format_to_date(val):
            if pd.isna(val) or val == "":
                return ""
            try:
                dt = pd.to_datetime(val)
                return dt.strftime("%Y/%m/%d")
            except Exception:
                return str(val)

        mapping = {
            "label_dendat": format_to_date(key_dendat),
            "label_tyuban": str(key_tyuban) if pd.notna(key_tyuban) else "",
            "label_nouki": format_to_date(key_nouki),
            "label_toknm1": str(key_toknm1) if pd.notna(key_toknm1) else "",
            "label_tanname": (
                str(first_row.get("TAN_NAME"))
                if pd.notna(first_row.get("TAN_NAME"))
                else ""
            ),
        }

        for label_name, val in mapping.items():
            if hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setText(val)

        if hasattr(self.ui, "tableWidget"):
            table = self.ui.tableWidget
            table.setRowCount(0)
            table.setRowCount(2 + (len(df_sub) * 2))

            def create_cell_item(
                val, is_numeric=False, align_center=False, is_header=False
            ):
                text = str(val) if pd.notna(val) else ""
                if is_numeric:
                    try:
                        num_val = float(val) if pd.notna(val) else 0.0
                        text = f"{int(num_val):,}"
                    except (ValueError, TypeError):
                        text = "0" if text == "" else text

                item = QTableWidgetItem(text)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                if is_header:
                    item.setBackground(QColor("#eff6ff"))
                    item.setForeground(QColor("#1e40af"))

                if align_center or is_header:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                elif is_numeric:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignRight
                        | Qt.AlignmentFlag.AlignVCenter
                    )
                else:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignLeft
                        | Qt.AlignmentFlag.AlignVCenter
                    )
                return item

            # --- 0行目（上段ヘッダー） ---
            table.setItem(0, 0, create_cell_item("受注番号", is_header=True))
            table.setItem(0, 1, create_cell_item("商品名", is_header=True))
            table.setItem(0, 2, create_cell_item("数量明細", is_header=True))
            table.setItem(0, 3, create_cell_item("単価", is_header=True))

            # --- 1行目（下段ヘッダー） ---
            table.setItem(1, 0, create_cell_item("", is_header=True))
            table.setItem(1, 1, create_cell_item("サイズ", is_header=True))
            table.setItem(
                1, 2, create_cell_item("客先仕様書No", is_header=True)
            )
            table.setItem(1, 3, create_cell_item("備考", is_header=True))

            table.setSpan(0, 0, 2, 1)
            table.setRowHeight(0, 20)
            table.setRowHeight(1, 20)

            for i in range(len(df_sub)):
                row = df_sub.iloc[i]
                top_row_idx = 2 + (i * 2)
                bottom_row_idx = top_row_idx + 1

                table.setItem(
                    top_row_idx,
                    0,
                    create_cell_item(row["JUH_JUHNO"], align_center=True),
                )
                table.setItem(bottom_row_idx, 0, QTableWidgetItem(""))

                table.setItem(top_row_idx, 1, create_cell_item(row["JUM_SHONM"]))
                table.setItem(
                    bottom_row_idx, 1, create_cell_item(row["JUM_KIKAKU"])
                )

                table.setItem(
                    top_row_idx, 2, create_cell_item(row["JUM_SURYOMEI"])
                )
                table.setItem(
                    bottom_row_idx, 2, create_cell_item(row["JUM_CUSTSYNO"])
                )

                table.setItem(
                    top_row_idx,
                    3,
                    create_cell_item(row["JUM_URITAN"], is_numeric=True),
                )
                table.setItem(
                    bottom_row_idx, 3, create_cell_item(row["JUM_BIKOU1"])
                )

                table.setSpan(top_row_idx, 0, 2, 1)
                table.setRowHeight(top_row_idx, 20)
                table.setRowHeight(bottom_row_idx, 20)

            table.viewport().update()

        print(
            f"【ログ】表示中: {self.current_group_idx + 1} / {len(self.grouped_keys)} グループ目"
        )

    def closeEvent(self, event):
        """画面が閉じられたときにメニュー画面(Tkinter)を再表示する"""
        if self.parent_root:
            self.parent_root.deiconify()
            self.parent_root.lift()
        event.accept()


def show_window(parent_root):
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = MyWindow(parent_root)
    window.show()
    app.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())