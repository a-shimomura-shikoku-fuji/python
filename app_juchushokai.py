import os
import sys
import pandas as pd
import common_utils

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QBrush, QColor, QFont, QIcon, QPen
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QMessageBox,
    QDateEdit,
    QPushButton,
    QStyledItemDelegate
)

class MyWindow:
    """受注照会システム メインウィンドウ管理クラス"""

    def __init__(self, parent_root=None, parent_menu=None):
        super().__init__()
        self.parent_root = parent_root
        self.parent_menu = parent_menu  # メニューのインスタンスを保持

        # --- 伝票めくり（ページング）機能用の変数初期化 ---
        self.current_group_idx = -1  # 現在表示中のグループインデックス
        self.grouped_keys = []        # グループ化された主キーのリスト
        self.all_details_df = None   # DBから取得した全明細データを保持するデータフレーム

        # 1. UIファイルの読み込み設定
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "app_juchushokai.ui")
        loader = QUiLoader()
        
        # デザイナーの設定（外枠レイアウト）を完全に保持したUIオブジェクトを生成
        self.ui = loader.load(ui_path)

        # 2. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.ui.setWindowTitle("受注照会")
        common_utils.set_common_window_icon(self.ui)
        self.ui.setFixedSize(self.ui.size()) 

        # クローズイベントをこのクラスの closeEvent メソッドに完全にフックする
        self.ui.closeEvent = self.closeEvent

        # 3. イベントシグナルの連携
        if hasattr(self.ui, "btn_exe_prev"):
            try: self.ui.btn_exe_prev.clicked.disconnect()
            except: pass
            self.ui.btn_exe_prev.clicked.connect(self.on_prevButton_click)

        if hasattr(self.ui, "btn_exe_next"):
            try: self.ui.btn_exe_next.clicked.disconnect()
            except: pass
            self.ui.btn_exe_next.clicked.connect(self.on_nextButton_click)

        if hasattr(self.ui, "btn_exe_inquiry"):
            try: self.ui.btn_exe_inquiry.clicked.disconnect()
            except: pass
            self.ui.btn_exe_inquiry.clicked.connect(self.load_initial_data)

        if hasattr(self.ui, "btn_clear"):
            try: self.ui.btn_clear.clicked.disconnect()
            except: pass
            self.ui.btn_clear.clicked.connect(self.clear_ui)

        # 4. 日付・テーブル類の接続と、強制初期化
        self.init_ui()              
        self.init_table_design()    
        self.clear_ui()             

        # UI内の「戻る」ボタンを全自動で探索して閉じるアクションを紐付け
        self.bind_back_button()

    def bind_back_button(self):
        """UI内の戻るボタンを自動検知して閉じるアクションを紐付ける"""
        if hasattr(self.ui, "btn_back"):
            self.ui.btn_back.clicked.connect(self.ui.close)
            return

        buttons = self.ui.findChildren(QPushButton)
        for btn in buttons:
            if btn.text() in ["戻る", "メニュー", "もどる", "Menu", "Back"]:
                print(f"【ログ】戻るボタンを自動検知しました: {btn.objectName()} -> {btn.text()}")
                btn.clicked.connect(self.ui.close)
                return

    def show(self):
        """ウィンドウを表示するメソッド"""
        self.ui.show()

    def init_ui(self):
        """検索条件の初期化とチェックボックスの連動設定"""
        disabled_style = """
            QDateEdit { color: black; background-color: #ffffff; }
            QDateEdit:disabled { color: #bbbbbb; background-color: #f1f5f9; }
        """

        for widget in [self.ui.date_nouki_from, self.ui.date_nouki_to, self.ui.date_juchu_date_from, self.ui.date_juchu_date_to]:
            widget.setDisplayFormat("yyyy/MM/dd")
            widget.setStyleSheet(disabled_style)
            try: widget.dateChanged.disconnect()
            except: pass

        # シグナル重複接続をリセット
        try: self.ui.chk_nouki.toggled.disconnect()
        except: pass
        try: self.ui.chk_juchu_date.toggled.disconnect()
        except: pass

        # チェックボックスと日付エリアの有効・無効化の連動
        self.ui.chk_nouki.toggled.connect(self.ui.date_nouki_from.setEnabled)
        self.ui.chk_nouki.toggled.connect(self.ui.date_nouki_to.setEnabled)
        self.ui.chk_juchu_date.toggled.connect(self.ui.date_juchu_date_from.setEnabled)
        self.ui.chk_juchu_date.toggled.connect(self.ui.date_juchu_date_to.setEnabled)

    # 1. まず、クラスの定義（MyWindowの上など、あるいは関数の直前）に罫線を描画するクラスを追加します。
    

    def init_table_design(self):
        """明細表示用テーブル（QTableWidget）の初期デザイン・列幅を設定する"""
        if not hasattr(self, "ui") or not hasattr(self.ui, "tableWidget"):
            print("【警告】UI上の tableWidget が見つかりません。")
            return

        table = self.ui.tableWidget
        table.setColumnCount(4)

        headers = [
            "受注番号",
            "商品名 / サイズ",
            "数量明細 / 客先仕様No",
            "単価 / 備考",
        ]
        table.setHorizontalHeaderLabels(headers)

        table.setColumnWidth(0, 115)
        table.setColumnWidth(1, 180)
        table.setColumnWidth(2, 200)
        table.setColumnWidth(3, 130)

        if hasattr(table, "verticalHeader"):
            table.verticalHeader().setVisible(False)

        print("【ログ】テーブルのデザイン適用が完了しました。")

    def load_initial_data(self):
        """【照会ボタン押下時】データベースから条件に該当するデータを取得して表示する"""
        print("【ログ】データの読み込みを開始します。")

        tyuban_val = ""
        if hasattr(self.ui, "text_chuban"):
            widget = self.ui.text_chuban
            if hasattr(widget, "text"):
                tyuban_val = widget.text().strip()
            elif hasattr(widget, "toPlainText"):
                tyuban_val = widget.toPlainText().strip()

        tanname_val = ""
        if hasattr(self.ui, "text_tanname"):
            widget = self.ui.text_tanname
            if hasattr(widget, "text"):
                tanname_val = widget.text().strip()
            elif hasattr(widget, "toPlainText"):
                tanname_val = widget.toPlainText().strip()

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
        
        nouki_f_val = self.ui.date_nouki_from.date().toString("yyyy-MM-dd") if self.ui.chk_nouki.isChecked() else ""
        nouki_t_val = self.ui.date_nouki_to.date().toString("yyyy-MM-dd") if self.ui.chk_nouki.isChecked() else ""
        
        dendat_f_val = self.ui.date_juchu_date_from.date().toString("yyyy-MM-dd") if self.ui.chk_juchu_date.isChecked() else ""
        dendat_t_val = self.ui.date_juchu_date_to.date().toString("yyyy-MM-dd") if self.ui.chk_juchu_date.isChecked() else ""

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

            if self.all_details_df.empty:
                QMessageBox.information(self.ui, "確認", "該当する data は見つかりませんでした。")
                self.clear_ui()
                return

            # 不整合の原因となる過剰な型変換を廃止し、空白のトリミングと欠損値補正のみ行う
            for col in ["JUH_DENDAT", "JUM_TYUBAN", "JUH_NOUKI", "JUH_TOKNM1", "JUH_TANCD"]:
                self.all_details_df[col] = self.all_details_df[col].fillna("")
                if self.all_details_df[col].dtype == object:
                    self.all_details_df[col] = self.all_details_df[col].astype(str).str.strip()

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

        labels_to_clear = ["data_juchu_date", "data_tok_chuban", "data_nouki", "data_tokname", "data_tanname", "word_count"]
        for label_name in labels_to_clear:
            if hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setText("")

        inputs_to_clear = ["text_chuban", "text_tanname"]
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

        # 日付選択の初期値とグレーアウトの確実な同期
        today = QDate.currentDate()
        self.ui.date_nouki_from.setDate(today)
        self.ui.date_nouki_to.setDate(today)
        self.ui.date_juchu_date_from.setDate(today.addMonths(-1))
        self.ui.date_juchu_date_to.setDate(today)

        # 一度TrueにしてからFalseに落とすことで、Qt内部のトグルイベントを確実に発火させグレーアウトさせる
        self.ui.chk_nouki.setChecked(True)
        self.ui.chk_juchu_date.setChecked(True)
        self.ui.chk_juchu_date.setChecked(False)

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

        if hasattr(self.ui, "word_count"):
            total_count = len(self.grouped_keys)
            current_num = self.current_group_idx + 1
            self.ui.word_count.setText(f"{current_num} / {total_count} 件")

        current_key = self.grouped_keys[self.current_group_idx]
        key_dendat, key_tyuban, key_nouki, key_toknm1, key_tancd = current_key

        # 生の型ブレ、NaN、空白を完全にクリアした安全な条件で完全一致抽出
        cond_dendat = (self.all_details_df["JUH_DENDAT"] == key_dendat) | (pd.isna(self.all_details_df["JUH_DENDAT"]) & pd.isna(key_dendat))
        cond_tyuban = (self.all_details_df["JUM_TYUBAN"] == key_tyuban) | (pd.isna(self.all_details_df["JUM_TYUBAN"]) & pd.isna(key_tyuban))
        cond_nouki = (self.all_details_df["JUH_NOUKI"] == key_nouki) | (pd.isna(self.all_details_df["JUH_NOUKI"]) & pd.isna(key_nouki))
        cond_toknm1 = (self.all_details_df["JUH_TOKNM1"] == key_toknm1) | (pd.isna(self.all_details_df["JUH_TOKNM1"]) & pd.isna(key_toknm1))
        cond_tancd = (self.all_details_df["JUH_TANCD"] == key_tancd) | (pd.isna(self.all_details_df["JUH_TANCD"]) & pd.isna(key_tancd))

        df_sub = self.all_details_df[cond_dendat & cond_tyuban & cond_nouki & cond_toknm1 & cond_tancd]

        if df_sub.empty:
            print("【デバッグ警告】マッチするデータ明細が存在しません。")
            return
            
        first_row = df_sub.iloc[0].to_dict()

        def format_to_date(val):
            if pd.isna(val) or str(val).strip() in ["", "nan", "NaT"]:
                return ""
            try:
                dt = pd.to_datetime(val)
                return dt.strftime("%Y/%m/%d")
            except Exception:
                return str(val).strip()

        mapping = {
            "data_juchu_date": format_to_date(key_dendat),
            "data_tok_chuban": str(key_tyuban).strip() if pd.notna(key_tyuban) and str(key_tyuban) != "nan" else "",
            "data_nouki": format_to_date(key_nouki),
            "data_tokname": str(key_toknm1).strip() if pd.notna(key_toknm1) and str(key_toknm1) != "nan" else "",
            "data_tanname": str(first_row.get("TAN_NAME")).strip() if pd.notna(first_row.get("TAN_NAME")) else "",
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

        print(f"运行中: 表示中: {self.current_group_idx + 1} / {len(self.grouped_keys)} グループ目")

    def closeEvent(self, event):
        """【★連動修正】画面を閉じる際、親メニュー画面を最前面に表示する"""
        print("【ログ】画面を閉じ、メニューを最前面に呼び出します。")
        if self.parent_menu and hasattr(self.parent_menu, "show_menu"):
            self.parent_menu.show_menu()
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

    # ヘッダーだけでなく、すべてのデータセルも太文字にする
    font = QFont()
    font. setBold(True)
    item. setFont(font)
    
    if is_header:
        item. setBackground( QColor("#94a3b8"))
        item. setForeground( QColor("#ffffff"))
    else:
        item. setBackground( QColor("#f1f5f9"))
        from PySide6.QtGui import QBrush
        item.setData(12, QBrush( QColor( "#94a3b8"))) 

    if align_center or is_header:
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    elif is_numeric:
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    else:
        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
    return item


def show_window(parent_root):
    """外部からこのPySide6ウィンドウを呼び出すためのエントリー関数"""
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
