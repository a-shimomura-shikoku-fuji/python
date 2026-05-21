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


class MyWindow:
    """受注照会システム メインウィンドウ管理クラス"""

    def __init__(self, parent_root=None, parent_menu=None):
        super().__init__()
        self.parent_root = parent_root
        self.parent_menu = parent_menu  # メニューのインスタンスを保持

        # --- 伝票めくり（ページング）機能用の変数初期化 ---
        self.current_group_idx = -1  # 現在表示中のグループインデックス
        self.grouped_keys = []        # グループ化された主キー the リスト
        self.all_details_df = None   # DBから取得した全明細データを保持するデータフレーム

        # 1. UIファイルの読み込み設定
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "app_juchushokai.ui")
        loader = QUiLoader()
        
        # 【★修正】引数にselfを渡さず、デザイナーの設定（外枠レイアウト）を完全に保持したUIオブジェクトを生成
        self.ui = loader.load(ui_path)

        # 2. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.ui.setWindowTitle(self.ui.windowTitle())
        self.ui.setWindowIcon(QIcon("my_logo.ico"))
        self.ui.setFixedSize(self.ui.size()) 

        # クローズイベントをフックするための特殊処理を設定
        self.ui.closeEvent = self.closeEvent

        # 3. イベントシグナルの連携
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

        # 4. 画面起動時の各種レイアウトの初期化
        self.init_ui()              # 日付コントロールの初期値設定
        self.init_table_design()    # テーブルレイアウトの初期化
        self.clear_ui()             # 起動時に一度クリアを呼んで初期化

         # 【★追加推奨】戻るボタン(btn_back)があれば、画面を閉じる処理を紐付けます
        if hasattr(self.ui, "btn_back"):
            self.ui.btn_back.clicked.connect(self.close)

    def show(self):
        """ウィンドウを表示するメソッド"""
        self.ui.show()

    def init_ui(self):
        """検索条件の初期化とチェックボックスの連動設定"""
        date_Nouki_F = self.ui.date_Nouki_F
        date_Nouki_T = self.ui.date_Nouki_T
        date_Dendat_F = self.ui.date_Dendat_F
        date_Dendat_T = self.ui.date_Dendat_T

        # スタイルシートで「無効時（:disabled）」の文字色をかなり薄いグレー（#bbbbbb）に指定
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

        tyuban_val = ""
        if hasattr(self.ui, "text_tyuban"):
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
        AND (? = '' OR JUM_TYUBAN LIKE ?)
        AND (? = '' OR TAN_NAME LIKE ?)
        ORDER BY JUH_DENDAT, JUM_TYUBAN, JUH_NOUKI, JUH_TOKNM1, JUH_TANCD
        """
        nouki_f_val = self.ui.date_Nouki_F.date().toString("yyyy-MM-dd") if self.ui.chk_Nouki.isChecked() else ""
        nouki_t_val = self.ui.date_Nouki_T.date().toString("yyyy-MM-dd") if self.ui.chk_Nouki.isChecked() else ""
        
        dendat_f_val = self.ui.date_Dendat_F.date().toString("yyyy-MM-dd") if self.ui.chk_Dendat.isChecked() else ""
        dendat_t_val = self.ui.date_Dendat_T.date().toString("yyyy-MM-dd") if self.ui.chk_Dendat.isChecked() else ""

        sql_params = [
            nouki_f_val, nouki_f_val, nouki_t_val,
            dendat_f_val, dendat_f_val, dendat_t_val,
            tyuban_val, f"%{tyuban_val}%",
            tanname_val, f"%{tanname_val}%"
        ]

        try:
            conn = common_utils.get_db_connection()
            self.all_details_df = pd.read_sql(sql, conn, params=sql_params)
            conn.close()

            # 【★修正】QMessageBoxの親を self から self.ui に変更
            if self.all_details_df.empty:
                QMessageBox.information(self.ui, "確認", "該当するデータは見つかりませんでした。")
                self.clear_ui()
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

            self.current_group_idx = 0
            print(f"【ログ】全明細を取得しました。件数: {len(self.all_details_df)} / グループ数: {len(self.grouped_keys)}")
            self._display_current_group()

        except Exception as e:
            # 【★修正】QMessageBoxの親を self から self.ui に変更
            QMessageBox.critical(
                self.ui,
                "エラー",
                f"データベース処理中にエラーが発生しました:\n{str(e)}",
            )
            self.clear_ui()

    def clear_ui(self):
        """【クリアボタン押下時】画面を初期起動時の状態に戻し、表示データをすべて削除する"""
        print("【ログ】画面上のデータをクリアします。")
        
        self.current_group_idx = -1
        self.grouped_keys = []
        self.all_details_df = None

        labels_to_clear = ["label_dendat", "label_tyuban", "label_nouki", "label_toknm1", "label_tanname", "label_Count"]
        for label_name in labels_to_clear:
            if hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setText("")

        inputs_to_clear = ["text_tyuban", "text_tanname"]
        for input_name in inputs_to_clear:
            if hasattr(self.ui, input_name):
                target = getattr(self.ui, input_name)
                if hasattr(target, "clear"):
                    target.clear()

        if hasattr(self.ui, "tableWidget"):
            table = self.ui.tableWidget
            table.setRowCount(0)
            
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

        self.ui.chk_Nouki.setChecked(True)
        self.ui.chk_Dendat.setChecked(False)

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
        if self.current_group_idx >= len(self.grouped_keys):
            self.current_group_idx = 0

        self._display_current_group()

    def on_prevButton_click(self):
        """「前へ」ボタン押下時、インデックスを1つ戻して前の伝票を表示する"""
        if self.all_details_df is None or not self.grouped_keys:
            return

        self.current_group_idx -= 1
        if self.current_group_idx < 0:
            self.current_group_idx = len(self.grouped_keys) - 1

        self._display_current_group()

    def _display_current_group(self):
        """現在選択されているインデックスの伝票ヘッダー情報および明細一覧を画面に描画する"""
        if not self.grouped_keys or self.all_details_df is None:
            return

        if hasattr(self.ui, "label_Count"):
            total_count = len(self.grouped_keys)
            current_num = self.current_group_idx + 1
            self.ui.label_Count.setText(f"{current_num} / {total_count} 件")

        current_key = self.grouped_keys[self.current_group_idx]
        key_dendat, key_tyuban, key_nouki, key_toknm1, key_tancd = current_key

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
            "label_tanname": str(first_row.get("TAN_NAME")) if pd.notna(first_row.get("TAN_NAME")) else "",
        }

        for label_name, val in mapping.items():
            if hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setText(val)

        if hasattr(self.ui, "tableWidget"):
            table = self.ui.tableWidget
            table.setRowCount(0)
            table.setRowCount(2 + (len(df_sub) * 2))

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

      # 【★修正】クローズイベントを書き換えます
    def closeEvent(self, event):
        """画面が閉じられたときに呼び出され、メニュー画面を再表示する"""
        if self.parent_menu:
            self.parent_menu.show_menu() # 親のメニュー画面を表示
        elif self.parent_root:
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
    window.show()  # 新設したshowメソッドで表示
    app.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()  # 新設したshowメソッドで表示
    sys.exit(app.exec())
