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
    QDateEdit
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

        # 「前へ」ボタン (pushButton_2) のイベント連携
        if hasattr(self.ui, "pushButton_2"):
            try:
                self.ui.pushButton_2.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_2.clicked.connect(self.on_prevButton_click)

        # 「次へ」ボタン (pushButton_3) のイベント連携
        if hasattr(self.ui, "pushButton_3"):
            try:
                self.ui.pushButton_3.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_3.clicked.connect(self.on_nextButton_click)

        # 「照会」ボタン (pushButton_9) のイベント連携
        if hasattr(self.ui, "pushButton_9"):
            try:
                self.ui.pushButton_9.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_9.clicked.connect(self.load_initial_data)

        # 「クリア」ボタン (pushButton_10) のイベント連携
        if hasattr(self.ui, "pushButton_10"):
            try:
                self.ui.pushButton_10.clicked.disconnect()
            except Exception:
                pass
            self.ui.pushButton_10.clicked.connect(self.clear_ui)

        # 5. 画面起動時の各種レイアウトの初期化
        self.init_ui()              # 日付コントロールの初期値設定
        self.init_table_design()    # テーブルレイアウトの初期化
        self.clear_ui()             # 【★修正】起動時に一度クリアを呼んでlabel_Countを含め初期化

    def init_ui(self):
        """検索条件の初期化とチェックボックスの連動設定"""
        date_Nouki_F = self.ui.date_Nouki_F
        date_Nouki_T = self.ui.date_Nouki_T
        date_Dendat_F = self.ui.date_Dendat_F
        date_Dendat_T = self.ui.date_Dendat_T

        # スタイルシートで「無効時（:disabled）」の文字色をかなり薄いグレー（#bbbbbb）に指定
        # 有効時は通常の黒（black）になります
        disabled_style = """
            QDateEdit { color: black; }
            QDateEdit:disabled { color: #bbbbbb; }
        """

        # 全ての日付コントロールの基本表示設定
        for widget in [date_Nouki_F, date_Nouki_T, date_Dendat_F, date_Dendat_T]:
            widget.setDisplayFormat("yyyy/MM/dd")
            widget.setStyleSheet(disabled_style)  # 薄いグレーのスタイルを適用
            try:
                widget.dateChanged.disconnect()
            except Exception:
                pass

        # 1. 初期日付の計算（本日、および1か月前）
        today = QDate.currentDate()
        one_month_ago = today.addMonths(-1)

        date_Nouki_F.setDate(today)
        date_Nouki_T.setDate(today)
        date_Dendat_F.setDate(one_month_ago)
        date_Dendat_T.setDate(today)

        # 2. チェックボックスの状態と日付欄の有効・無効（グレーアウト）を連動
        self.ui.chk_Nouki.toggled.connect(date_Nouki_F.setEnabled)
        self.ui.chk_Nouki.toggled.connect(date_Nouki_T.setEnabled)
        self.ui.chk_Dendat.toggled.connect(date_Dendat_F.setEnabled)
        self.ui.chk_Dendat.toggled.connect(date_Dendat_T.setEnabled)

    def init_table_design(self):
        """明細表示用テーブル（QTableWidget）の初期デザイン・列幅を設定する"""
        if not hasattr(self, "ui") or not hasattr(self.ui, "tableWidget"):
            print("【警告】UI上の tableWidget が見つかりません。")
            return

        table = self.ui.tableWidget
        table.setColumnCount(4)

        # ヘッダーラベルの設定
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
        """【照会ボタン押下時】データベースから条件に該当するデータを取得して表示する"""
        print("【ログ】データの読み込みを開始します。")

        # 【★新規追加】テキスト入力欄（注番・担当者名）からの値取得処理
        tyuban_val = ""
        if hasattr(self.ui, "text_tyuban"):
            # QLineEditならtext()、QTextEditならtoPlainText()で安全に取得
            if hasattr(self.ui.text_tyuban, "text"):
                tyuban_val = self.ui.text_tyuban.text().strip()
            elif hasattr(self.ui.text_tyuban, "toPlainText"):
                tyuban_val = self.ui.text_tyuban.toPlainText().strip()

        tanname_val = ""
        if hasattr(self.ui, "text_tanname"):
            if hasattr(self.ui.text_tanname, "text"):
                tanname_val = self.ui.text_tanname.text().strip()
            elif hasattr(self.ui.text_tanname, "toPlainText"):
                tanname_val = self.ui.text_tanname.toPlainText().strip()

        # 受注データおよび明細データを結合取得するSQL
        # 【★修正】JUM_TYUBAN と TAN_NAME の部分一致（LIKE）条件を追加
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
        WHERE (? = '' OR JUH_NOUKI BETWEEN ? AND ?)
        AND (? = '' OR JUH_DENDAT BETWEEN ? AND ?)    
        AND (? = '' OR JUH_CHUBAN LIKE ?)
        AND (? = '' OR TAN_NAME LIKE ?)
        ORDER BY JUH_DENDAT, JUM_TYUBAN, JUH_NOUKI, JUH_TOKNM1, JUH_TANCD
        """
        # チェックボックスがONなら日付文字列、OFFなら空文字（条件無視）にする
        nouki_f_val = self.ui.date_Nouki_F.date().toString("yyyy-MM-dd") if self.ui.chk_Nouki.isChecked() else ""
        nouki_t_val = self.ui.date_Nouki_T.date().toString("yyyy-MM-dd") if self.ui.chk_Nouki.isChecked() else ""
        
        dendat_f_val = self.ui.date_Dendat_F.date().toString("yyyy-MM-dd") if self.ui.chk_Dendat.isChecked() else ""
        dendat_t_val = self.ui.date_Dendat_T.date().toString("yyyy-MM-dd") if self.ui.chk_Dendat.isChecked() else ""

        # SQLパラメータのリスト作成
        sql_params = [
            nouki_f_val, nouki_f_val, nouki_t_val,     # 納期用
            dendat_f_val, dendat_f_val, dendat_t_val,   # 受注日用
            tyuban_val, f"%{tyuban_val}%",
            tanname_val, f"%{tanname_val}%"
        ]

        try:
            # データベース接続とデータ読込の実行
            conn = common_utils.get_db_connection()
            self.all_details_df = pd.read_sql(sql, conn, params=sql_params)
            conn.close()

            # データが存在しない場合の処理
            if self.all_details_df.empty:
                QMessageBox.information(self, "確認", "該当するデータは見つかりませんでした。")
                self.clear_ui()  # 既存のデータを画面から綺麗にする
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
            self.clear_ui()

    def clear_ui(self):
        """【クリアボタン押下時】画面を初期起動時の状態に戻し、表示データをすべて削除する"""
        print("【ログ】画面上のデータをクリアします。")
        
        # 1. 内部保持データの初期化
        self.current_group_idx = -1
        self.grouped_keys = []
        self.all_details_df = None

        # 2. 上部ヘッダーのテキストラベルを空文字に（label_Countもここに含まれます）
        labels_to_clear = ["label_dendat", "label_tyuban", "label_nouki", "label_toknm1", "label_tanname", "label_Count"]
        for label_name in labels_to_clear:
            if hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setText("")

        # 【★新規追加】検索用入力テキスト（text_tyuban / text_tanname）もクリアする
        inputs_to_clear = ["text_tyuban", "text_tanname"]
        for input_name in inputs_to_clear:
            if hasattr(self.ui, input_name):
                target = getattr(self.ui, input_name)
                if hasattr(target, "clear"):
                    target.clear()

        # 3. テーブル明細行の初期化
        if hasattr(self.ui, "tableWidget"):
            table = self.ui.tableWidget
            table.setRowCount(0)
            
            # 再びヘッダー2行のみを構築し直す
            table.setRowCount(2)
            table.setItem(0, 0, create_cell_item_helper("受注番号", is_header=True))
            table.setItem(0, 1, create_cell_item_helper("商品名", is_header=True))
            table.setItem(0, 2, create_cell_item_helper("数量明細", is_header=True))
            table.setItem(0, 3, create_cell_item_helper("単価", is_header=True))
            table.setItem(1, 0, create_cell_item_helper("", is_header=True))
            table.setItem(1, 1, create_cell_item_helper("サイズ", is_header=True))
            table.setItem(1, 2, create_cell_item_helper("客先仕様書No", is_header=True))
            table.setItem(1, 3, create_cell_item_helper("備考", is_header=True))
            table.setSpan(0, 0, 2, 1)
            table.setRowHeight(0, 20)
            table.setRowHeight(1, 20)
            table.viewport().update()

        # 4. 日付入力欄のチェックボックスを解除（受注日は指定なし・グレーアウトにする）
        self.ui.chk_Nouki.setChecked(True)
        self.ui.chk_Dendat.setChecked(False)

        # 日付自体も初期値（直近1か月/本日）にリセット
        today = QDate.currentDate()
        self.ui.date_Nouki_F.setDate(today)
        self.ui.date_Nouki_T.setDate(today)
        self.ui.date_Dendat_F.setDate(today.addMonths(-1))
        self.ui.date_Dendat_T.setDate(today.addDays(-1))

    def on_nextButton_click(self):
        """「次へ」ボタン押下時、インデックスを1つ進めて次の伝票を表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        self.current_group_idx += 1

        # 最後のデータを超えたら、最初のデータに戻る
        if self.current_group_idx >= len(self.grouped_keys):
            self.current_group_idx = 0

        self._display_current_group()

    def on_prevButton_click(self):
        """「前へ」ボタン押下時、インデックスを1つ戻して前の伝票を表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        self.current_group_idx -= 1

        # 最初のデータを下回ったら、最後のデータに移動する
        if self.current_group_idx < 0:
            self.current_group_idx = len(self.grouped_keys) - 1

        self._display_current_group()

    def _display_current_group(self):
        """現在選択されているインデックスの伝票ヘッダー情報および明細一覧を画面に描画する"""
        if not self.grouped_keys or self.all_details_df is None:
            return

        # label_Count に進捗を表示
        if hasattr(self.ui, "label_Count"):
            total_count = len(self.grouped_keys)
            current_num = self.current_group_idx + 1
            self.ui.label_Count.setText(f"{current_num} / {total_count} 件")

        # 現在のグループキー情報を展開
        current_key = self.grouped_keys[self.current_group_idx]
        key_dendat, key_tyuban, key_nouki, key_toknm1, key_tancd = current_key

        # 全明細から、現在のグループキーに完全一致する明細行だけをフィルタリング
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

        # 各ラベルへのマッピング
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
            table.setRowCount(2 + (len(df_sub) * 2))

            # 上段・下段ヘッダーを設置
            table.setItem(0, 0, create_cell_item_helper("受注番号", is_header=True))
            table.setItem(0, 1, create_cell_item_helper("商品名", is_header=True))
            table.setItem(0, 2, create_cell_item_helper("数量明細", is_header=True))
            table.setItem(0, 3, create_cell_item_helper("単価", is_header=True))
            table.setItem(1, 0, create_cell_item_helper("", is_header=True))
            table.setItem(1, 1, create_cell_item_helper("サイズ", is_header=True))
            table.setItem(1, 2, create_cell_item_helper("客先仕様書No", is_header=True))
            table.setItem(1, 3, create_cell_item_helper("備考", is_header=True))
            table.setSpan(0, 0, 2, 1)
            table.setRowHeight(0, 20)
            table.setRowHeight(1, 20)

            # 各明細データのループ挿入
            for i in range(len(df_sub)):
                row = df_sub.iloc[i]
                top_row_idx = 2 + (i * 2)
                bottom_row_idx = top_row_idx + 1

                table.setItem(top_row_idx, 0, create_cell_item_helper(row["JUH_JUHNO"], align_center=True))
                table.setItem(bottom_row_idx, 0, QTableWidgetItem(""))

                table.setItem(top_row_idx, 1, create_cell_item_helper(row["JUM_SHONM"]))
                table.setItem(bottom_row_idx, 1, create_cell_item_helper(row["JUM_KIKAKU"]))

                table.setItem(top_row_idx, 2, create_cell_item_helper(row["JUM_SURYOMEI"]))
                table.setItem(bottom_row_idx, 2, create_cell_item_helper(row["JUM_CUSTSYNO"]))

                table.setItem(top_row_idx, 3, create_cell_item_helper(row["JUM_URITAN"], is_numeric=True))
                table.setItem(bottom_row_idx, 3, create_cell_item_helper(row["JUM_BIKOU1"]))

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


def create_cell_item_helper(val, is_numeric=False, align_center=False, is_header=False):
    """QTableWidgetItem を生成・装飾する共通ヘルパー関数"""
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
        
        # フォントオブジェクトを作成し、太字（Bold）に設定してセルに適用する
        font = QFont()
        font.setBold(True)
        item.setFont(font)

    if align_center or is_header:
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    elif is_numeric:
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    else:
        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
    return item


def show_window(parent_root):
    """外部（Tkinter側など）からこのPySide6ウィンドウを呼び出すためのエントリー関数"""
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
