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
    """受注照会システム メインウィンドウクラス"""

    def __init__(self, parent_root=None):
        super().__init__()
        self.parent_root = parent_root

        # --- 伝票めくり（ページング）機能用の変数初期化 ---
        self.current_group_idx = -1  # 現在表示中のグループインデックス
        self.grouped_keys = []        # グループ化された主キーのリスト
        self.all_details_df = None   # DBから取得した全明細データを保持するデータフレーム

        # 1. UIファイルの読み込み設定
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "app_juchushokai.ui")
        loader = QUiLoader()
        loaded_ui = loader.load(ui_path)

        # 2. メイン画面の構築とUI構造の移植
        self.setCentralWidget(loaded_ui.centralWidget())

        # UIファイルに設定されたスタイルシート（背景色・フォント等）をウィンドウ全体に適用
        self.setStyleSheet(loaded_ui.styleSheet())

        if hasattr(loaded_ui, "menuBar") and loaded_ui.menuBar():
            self.setMenuBar(loaded_ui.menuBar())
        if hasattr(loaded_ui, "statusBar") and loaded_ui.statusBar():
            self.setStatusBar(loaded_ui.statusBar())

        # 3. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.resize(loaded_ui.size())
        self.setWindowTitle(loaded_ui.windowTitle())
        self.setWindowIcon(QIcon("my_logo.ico"))

        # 4. UIオブジェクトの保持とイベントシグナルの連携
        self.ui = loaded_ui

        # 「前へ」ボタン (pushButton_2) のイベント連携（重複接続防止のため一度切断）
        if hasattr(self.ui, "pushButton_2"):
            try:
                self.ui.pushButton_2.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_2.clicked.connect(self.on_prevButton_click)

        # 「次へ」ボタン (pushButton_3) のイベント連携（重複接続防止のため一度切断）
        if hasattr(self.ui, "pushButton_3"):
            try:
                self.ui.pushButton_3.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_3.clicked.connect(self.on_nextButton_click)

        # 画面起動時の初期化処理
        self.init_ui()              # 日付コントロールの初期化
        self.init_table_design()    # テーブルレイアウトの初期化
        self.load_initial_data()    # データベースからのデータ自動読み込み

    def init_ui(self):
        """検索条件の日付入力欄（QDateEdit）に初期値を設定する"""
        date_Nouki_F = self.ui.date_Nouki_F
        date_Nouki_T = self.ui.date_Nouki_T
        date_Dendat_F = self.ui.date_Dendat_F
        date_Dendat_T = self.ui.date_Dendat_T

        # 納期条件：デフォルトは「本日 ～ 本日」
        date_Nouki_F.setDate(QDate.currentDate())
        date_Nouki_T.setDate(QDate.currentDate())
        # 伝票日付条件：デフォルトは「1年前 ～ 昨日」
        date_Dendat_F.setDate(QDate.currentDate().addYears(-1))
        date_Dendat_T.setDate(QDate.currentDate().addDays(-1))

    def init_table_design(self):
        """明細表示用テーブル（QTableWidget）の初期デザイン・列幅を設定する"""
        if not hasattr(self, "ui") or not hasattr(self.ui, "tableWidget"):
            print("【警告】UI上の tableWidget が見つかりません。")
            return

        table = self.ui.tableWidget
        table.setColumnCount(4)

        # ヘッダーラベルの設定（2段組レイアウトを想定）
        headers = [
            "受注番号",
            "商品名 / サイズ",
            "数量明細 / 客先仕様No",
            "単価 / 備考",
        ]
        table.setHorizontalHeaderLabels(headers)

        # 各列の幅を最適化
        table.setColumnWidth(0, 100)
        table.setColumnWidth(1, 180)
        table.setColumnWidth(2, 200)
        table.setColumnWidth(3, 130)

        # 行番号（垂直ヘッダー）を非表示にする
        if hasattr(table, "verticalHeader"):
            table.verticalHeader().setVisible(False)

        print("【ログ】テーブルのデザイン適用が完了しました。")

    def load_initial_data(self):
        """画面起動時にデータベースから条件に該当する全件を取得し、1件目を表示する"""
        print("【ログ】初期データの読み込みを開始します。")

        # 受注データおよび明細データを結合取得するSQL（SQLite/SQL Server等のプレースホルダ形式）
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

        # SQLパラメータのリスト作成（SQL内の「?」に順番にマッピングされます）
        sql_params = [
            self.ui.date_Nouki_F.date().toString("yyyy-MM-dd"),
            self.ui.date_Nouki_T.date().toString("yyyy-MM-dd"),
            self.ui.date_Dendat_F.date().toString("yyyy-MM-dd"),
            self.ui.date_Dendat_T.date().toString("yyyy-MM-dd")
        ]

        try:
            # データベース接続とデータ読込の実行
            conn = common_utils.get_db_connection()
            self.all_details_df = pd.read_sql(sql, conn, params=sql_params)
            conn.close()

            # データが存在しない場合の処理
            if self.all_details_df.empty:
                QMessageBox.information(self, "確認", "該当するデータは見つかりませんでした。")
                self.all_details_df = None
                return

            # 伝票（グループ）の単位となる主キーを設定
            group_keys = [
                "JUH_DENDAT",
                "JUM_TYUBAN",
                "JUH_NOUKI",
                "JUH_TOKNM1",
                "JUH_TANCD",
            ]
            # 重複を排除してグループのリストを生成
            self.grouped_keys = list(
                self.all_details_df[group_keys]
                .drop_duplicates()
                .itertuples(index=False, name=None)
            )

            # 初期表示として最初のグループ（インデックス0）を指定
            self.current_group_idx = 0

            print(f"【ログ】全明細を取得しました。件数: {len(self.all_details_df)} / グループ数: {len(self.grouped_keys)}")
            self._display_current_group()

        except Exception as e:
            QMessageBox.critical(
                self,
                "エラー",
                f"データベース処理中にエラーが発生しました:\n{str(e)}",
            )
            self.all_details_df = None

    def on_nextButton_click(self):
        """「次へ」ボタン押下時、インデックスを1つ進めて次の伝票を表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        self.current_group_idx += 1

        # 最後のデータを超えたら、最初のデータ（インデックス0）に戻る
        if self.current_group_idx >= len(self.grouped_keys):
            QMessageBox.information(self, "確認", "最後のデータです。最初のデータに戻ります。")
            self.current_group_idx = 0

        self._display_current_group()

    def on_prevButton_click(self):
        """「前へ」ボタン押下時、インデックスを1つ戻して前の伝票を表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        self.current_group_idx -= 1

        # 最初のデータを下回ったら、最後のデータ（末尾のインデックス）に移動する
        if self.current_group_idx < 0:
            QMessageBox.information(self, "確認", "最初のデータです。最後のデータに移動します。")
            self.current_group_idx = len(self.grouped_keys) - 1

        self._display_current_group()

    def _display_current_group(self):
        """現在選択されているインデックスの伝票ヘッダー情報および明細一覧を画面に描画する"""
        if not self.grouped_keys or self.all_details_df is None:
            return

        # 現在のグループキー情報を展開
        current_key = self.grouped_keys[self.current_group_idx]
        key_dendat, key_tyuban, key_nouki, key_toknm1, key_tancd = current_key

        # 全明細から、現在のグループキーに完全一致する明細行だけをフィルタリング（NaN値の判定含む）
        df_sub = self.all_details_df[
            (
                (self.all_details_df["JUH_DENDAT"] == key_dendat)

                | (pd.isna(self.all_details_df["JUH_DENDAT"]) & pd.isna(key_dendat))
            )
            & (
                (self.all_details_df["JUM_TYUBAN"] == key_tyuban)
                | (pd.isna(self.all_details_df["JUM_TYUBAN"]) & pd.isna(key_tyuban))
            )
            & (
                (self.all_details_df["JUH_NOUKI"] == key_nouki)

                | (pd.isna(self.all_details_df["JUH_NOUKI"]) & pd.isna(key_nouki))
            )
            & (
                (self.all_details_df["JUH_TOKNM1"] == key_toknm1)
                | (pd.isna(self.all_details_df["JUH_TOKNM1"]) & pd.isna(key_toknm1))
            )
            & (
                (self.all_details_df["JUH_TANCD"] == key_tancd)

                | (pd.isna(self.all_details_df["JUH_TANCD"]) & pd.isna(key_tancd))
            )
        ]

        first_row = df_sub.iloc[0].to_dict()

        def format_to_date(val):
            """日付データを yyyy/mm/dd 形式の文字列にフォーマットする内部関数"""
            if pd.isna(val) or val == "":
                return ""
            try:
                dt = pd.to_datetime(val)
                return dt.strftime("%Y/%m/%d")
            except Exception:
                return str(val)

        # 画面上部等のヘッダーテキストラベルへのマッピングマッピング
        mapping = {
            "label_dendat": format_to_date(key_dendat),
            "label_tyuban": str(key_tyuban) if pd.notna(key_tyuban) else "",
            "label_nouki": format_to_date(key_nouki),
            "label_toknm1": str(key_toknm1) if pd.notna(key_toknm1) else "",
            "label_tanname": str(first_row.get("TAN_NAME")) if pd.notna(first_row.get("TAN_NAME")) else "",
        }

        for label_name, val in mapping.items():
            if hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setText(val)

        # --- テーブル Widget への明細描画処理 ---
        if hasattr(self.ui, "tableWidget"):
            table = self.ui.tableWidget
            table.setRowCount(0)
            # ヘッダー2行 ＋ (明細データ数 × 上下2行構成) の行数を確保
            table.setRowCount(2 + (len(df_sub) * 2))

            def create_cell_item(val, is_numeric=False, align_center=False, is_header=False):
                """QTableWidgetItem を生成・装飾する内部共通関数"""
                text = str(val) if pd.notna(val) else ""
                if is_numeric:
                    try:
                        num_val = float(val) if pd.notna(val) else 0.0
                        text = f"{int(num_val):,}"  # カンマ区切り整数フォーマット
                    except (ValueError, TypeError):
                        text = "0" if text == "" else text

                item = QTableWidgetItem(text)
                # セルをダブルクリック等で編集できないように読み取り専用フラグを設定
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                # ヘッダー行用のスタイル設定（薄い青の背景、濃い青の文字）
                if is_header:
                    item.setBackground(QColor("#eff6ff"))
                    item.setForeground(QColor("#1e40af"))

                # 配置（アライメント）の決定
                if align_center or is_header:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                elif is_numeric:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                else:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                return item

            # --- 0行目（上段ヘッダー定義） ---
            table.setItem(0, 0, create_cell_item("受注番号", is_header=True))
            table.setItem(0, 1, create_cell_item("商品名", is_header=True))
            table.setItem(0, 2, create_cell_item("数量明細", is_header=True))
            table.setItem(0, 3, create_cell_item("単価", is_header=True))

            # --- 1行目（下段ヘッダー定義） ---
            table.setItem(1, 0, create_cell_item("", is_header=True))
            table.setItem(1, 1, create_cell_item("サイズ", is_header=True))
            table.setItem(1, 2, create_cell_item("客先仕様書No", is_header=True))
            table.setItem(1, 3, create_cell_item("備考", is_header=True))

            # 「受注番号」ヘッダーの上下結合（0行目から2行分、1列分を結合）
            table.setSpan(0, 0, 2, 1)
            table.setRowHeight(0, 20)
            table.setRowHeight(1, 20)

            # --- 2行目以降（明細データ行）のループ展開 ---
            for i in range(len(df_sub)):
                row = df_sub.iloc[i]
                top_row_idx = 2 + (i * 2)
                bottom_row_idx = top_row_idx + 1

                # 左端：受注番号のセル配置（上下結合）
                table.setItem(top_row_idx, 0, create_cell_item(row["JUH_JUHNO"], align_center=True))
                table.setItem(bottom_row_idx, 0, QTableWidgetItem(""))

                # 2列目：商品名（上段） / サイズ（下段）
                table.setItem(top_row_idx, 1, create_cell_item(row["JUM_SHONM"]))
                table.setItem(bottom_row_idx, 1, create_cell_item(row["JUM_KIKAKU"]))

                # 3列目：数量明細（上段） / 客先仕様書No（下段）
                table.setItem(top_row_idx, 2, create_cell_item(row["JUM_SURYOMEI"]))
                table.setItem(bottom_row_idx, 2, create_cell_item(row["JUM_CUSTSYNO"]))

                # 4列目：単価（上段・数値） / 備考（下段）
                table.setItem(top_row_idx, 3, create_cell_item(row["JUM_URITAN"], is_numeric=True))
                table.setItem(bottom_row_idx, 3, create_cell_item(row["JUM_BIKOU1"]))

                # 明細内の「受注番号」セルの上下結合と行高の設定
                table.setSpan(top_row_idx, 0, 2, 1)
                table.setRowHeight(top_row_idx, 20)
                table.setRowHeight(bottom_row_idx, 20)

            table.viewport().update()

        print(f"【ログ】表示中: {self.current_group_idx + 1} / {len(self.grouped_keys)} グループ目")

    def closeEvent(self, event):
        """画面が閉じられたときに呼び出され、呼び出し元のTkinterメニュー画面を再表示する"""
        if self.parent_root:
            self.parent_root.deiconify()
            self.parent_root.lift()
        event.accept()


def show_window(parent_root):
    """外部（Tkinter側など）からこのPySide6ウィンドウを呼び出すためのエントリー関数"""
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = MyWindow(parent_root)
    window.show()
    app.exec()


if __name__ == "__main__":
    # 単体起動テスト用処理
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())