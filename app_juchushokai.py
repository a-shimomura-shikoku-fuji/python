# -*- coding: utf-8 -*-
import calendar
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
import pandas as pd
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QIcon, QPen
from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QMessageBox,
    QDateEdit,
    QPushButton
)
# 💡 app_nouhin.py と完全に同じ loadUiType 手続き
from PySide6.QtUiTools import loadUiType

# 共通ユーティリティのインポート
import common_utils

# Pythonに古い一時ファイル（.pyc）を作らせない設定
sys.dont_write_bytecode = True

# --- 💡 app_nouhin.py と同様の手続きでUIファイルをロード ---
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
ui_path = os.path.join(root_dir, "ui_files", "app_juchushokai.ui")
Ui_MainWindow, QMainWindowBase = loadUiType(ui_path)

# --- QTableWidgetの最大列数と各列幅の定数化 ---
TABLE_TOTAL_COLUMNS = 4
COL_WIDTH_ORDER_NO = 115 # 受注番号列
COL_WIDTH_PRODUCT = 180  # 商品名 / サイズ列
COL_WIDTH_DETAIL = 200   # 数量明細 / 客先仕様No列
COL_WIDTH_PRICE = 130    # 単価 / 備考列


# 💡 app_nouhin.py と同じく多重継承構造に変更
class MyWindow(QMainWindowBase, Ui_MainWindow):
    """受注照会システム メインウィンドウ管理クラス"""

    def __init__(self, parent_root=None, parent_menu=None):
        """初期化処理・コンポーネントとUIのセットアップ"""
        super().__init__()
        self.parent_root = parent_root
        self.parent_menu = parent_menu

        # --- 伝票めくり（ページング）機能用の変数初期化 ---
        self.current_group_idx = -1
        self.grouped_keys = []
        self.all_details_df = None

        # 💡 読み込んだUI定義を自分自身にセットアップ
        self.setupUi(self)

        # 2. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.setWindowTitle("受注照会")
        common_utils.set_common_window_icon(self)
        self.setFixedSize(self.size())

        # 3. イベントシグナル（ボタン）の連携
        if hasattr(self, "btn_exe_prev"):
            try:
                self.btn_exe_prev.clicked.disconnect()
            except:
                pass
            self.btn_exe_prev.clicked.connect(self.on_prevButton_click)

        if hasattr(self, "btn_exe_next"):
            try:
                self.btn_exe_next.clicked.disconnect()
            except:
                pass
            self.btn_exe_next.clicked.connect(self.on_nextButton_click)

        if hasattr(self, "btn_exe_inquiry"):
            try:
                self.btn_exe_inquiry.clicked.disconnect()
            except:
                pass
            self.btn_exe_inquiry.clicked.connect(self.load_initial_data)

        if hasattr(self, "btn_clear"):
            try:
                self.btn_clear.clicked.disconnect()
            except:
                pass
            self.btn_clear.clicked.connect(self.clear_ui)

        # 4. 日付・テーブル類の接続と、初期化
        self.init_ui()
        self.init_table_design()
        self.clear_ui()

        # UI内の「戻る」ボタンのアクション紐付け
        self.bind_back_button()
    def bind_back_button(self):
        """UI内の戻るボタンを自動検知して閉じるアクションを紐付ける"""
        if hasattr(self, "btn_back"):
            self.btn_back.clicked.connect(self.close)
            return

        buttons = self.findChildren(QPushButton)
        for btn in buttons:
            if btn.text() in ["戻る", "メニュー", "もどる", "Menu", "Back"]:
                btn.clicked.connect(self.close)
                return

    def init_ui(self):
        """検索条件の初期化とチェックボックスの連動設定"""
        disabled_style = """
        QDateEdit { color: black; background-color: #ffffff; }
        QDateEdit:disabled { color: #bbbbbb; background-color: #f1f5f9; }
        """
        # 💡 self.ui. を外して、直接コントロールにアクセス
        date_widgets = [
            self.date_nouki_from,
            self.date_nouki_to,
            self.date_juchu_date_from,
            self.date_juchu_date_to
        ]

        for widget in date_widgets:
            widget.setDisplayFormat("yyyy/MM/dd")
            widget.setStyleSheet(disabled_style)
            try:
                widget.dateChanged.disconnect()
            except:
                pass

        try:
            self.chk_nouki.toggled.disconnect()
        except:
            pass
        try:
            self.chk_juchu_date.toggled.disconnect()
        except:
            pass

        # チェックボックスと日付エリアの有効・無効化の連動
        self.chk_nouki.toggled.connect(self.date_nouki_from.setEnabled)
        self.chk_nouki.toggled.connect(self.date_nouki_to.setEnabled)
        self.chk_juchu_date.toggled.connect(self.date_juchu_date_from.setEnabled)
        self.chk_juchu_date.toggled.connect(self.date_juchu_date_to.setEnabled)

        # ★ 【共通部品化】ダミーボタンのTabフォーカスを無効化
        common_utils.disable_dummy_buttons_tab_focus(self)
        # ★ 【共通部品化】すべての複数行テキストエリアでTabキー移動を有効化
        common_utils.setup_text_edits_tab_focus(self)

    def init_table_design(self):
        """明細表示用テーブル（QTableWidget）の初期デザイン・列幅を設定する"""
        if not hasattr(self, "tableWidget"):
            return

        table = self.tableWidget
        table.setColumnCount(TABLE_TOTAL_COLUMNS)
        headers = [
            "受注番号",
            "商品名 / サイズ",
            "数量明細 / 客先仕様No",
            "単価 / 備考",
        ]
        table.setHorizontalHeaderLabels(headers)
        table.setColumnWidth(0, COL_WIDTH_ORDER_NO)
        table.setColumnWidth(1, COL_WIDTH_PRODUCT)
        table.setColumnWidth(2, COL_WIDTH_DETAIL)
        table.setColumnWidth(3, COL_WIDTH_PRICE)

        if hasattr(table, "verticalHeader"):
            table.verticalHeader().setVisible(False)

    def load_initial_data(self):
        """【照会ボタン押下時】データベースから条件に該当するデータを取得して表示する"""
        tyuban_val = ""
        if hasattr(self, "text_chuban"):
            widget = self.text_chuban
            if hasattr(widget, "text"):
                tyuban_val = widget.text().strip()
            elif hasattr(widget, "toPlainText"):
                tyuban_val = widget.toPlainText().strip()

        tanname_val = ""
        if hasattr(self, "text_tanname"):
            widget = self.text_tanname
            if hasattr(widget, "text"):
                tanname_val = widget.text().strip()
            elif hasattr(widget, "toPlainText"):
                tanname_val = widget.toPlainText().strip()

        sql = """
        SELECT
            JUH_DENDAT, JUH_JUHNO, JUM_TYUBAN, JUH_NOUKI, JUH_TOKNM1, JUH_TANCD,
            TAN_NAME, JUM_SHONM, JUM_KIKAKU, JUM_SURYOMEI, JUM_CUSTSYNO, JUM_URITAN, JUM_BIKOU1
        FROM T_JUHDAT
        INNER JOIN T_JUMDAT ON JUH_KCODE = JUM_KCODE AND JUH_DENNO = JUM_DENNO
        LEFT OUTER JOIN T_TANMST ON JUH_TANCD = TAN_CODE
        WHERE (? = '' OR JUH_NOUKI BETWEEN ? AND ?)
          AND (? = '' OR JUH_DENDAT BETWEEN ? AND ?)
          AND (? = '' OR JUM_TYUBAN LIKE ?)
          AND (? = '' OR TAN_NAME LIKE ?)
        ORDER BY JUH_DENDAT, JUM_TYUBAN, JUH_NOUKI, JUH_TOKNM1, JUH_TANCD
        """

        nouki_f_val = self.date_nouki_from.date().toString("yyyy-MM-dd") if self.chk_nouki.isChecked() else ""
        nouki_t_val = self.date_nouki_to.date().toString("yyyy-MM-dd") if self.chk_nouki.isChecked() else ""
        dendat_f_val = self.date_juchu_date_from.date().toString("yyyy-MM-dd") if self.chk_juchu_date.isChecked() else ""
        dendat_t_val = self.date_juchu_date_to.date().toString("yyyy-MM-dd") if self.chk_juchu_date.isChecked() else ""

        sql_params = [
            nouki_f_val, nouki_f_val, nouki_t_val,
            dendat_f_val, dendat_f_val, dendat_t_val,
            tyuban_val, f"%{tyuban_val}%",
            tanname_val, f"%{tanname_val}%"
        ]

        conn = common_utils.get_db_connection()
        try:
            self.all_details_df = pd.read_sql(sql, conn, params=sql_params)
            if self.all_details_df.empty:
                QMessageBox.information(self, "確認", "該当するデータは見つかりませんでした。")
                return

            for col in ["JUH_DENDAT", "JUM_TYUBAN", "JUH_NOUKI", "JUH_TOKNM1", "JUH_TANCD"]:
                self.all_details_df[col] = self.all_details_df[col].fillna("")
                if self.all_details_df[col].dtype == object:
                    self.all_details_df[col] = self.all_details_df[col].astype(str).str.strip()

            group_keys = ["JUH_DENDAT", "JUM_TYUBAN", "JUH_NOUKI", "JUH_TOKNM1", "JUH_TANCD"]
            self.grouped_keys = list(self.all_details_df[group_keys].drop_duplicates().itertuples(index=False, name=None))
            self.current_group_idx = 0
            self._display_current_group()
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"データベース処理中にエラーが発生しました:\n{str(e)}")
            self.clear_ui()
        finally:
            conn.close()
    def clear_ui(self):
        """【クリアボタン（btn_clear）押下時】画面を初期状態に戻す"""
        self.current_group_idx = -1
        self.grouped_keys = []
        self.all_details_df = None

        labels = ["data_juchu_date", "data_tok_chuban", "data_nouki", "data_tokname", "data_tanname", "word_count"]
        for lbl in labels:
            if hasattr(self, lbl):
                getattr(self, lbl).setText("")

        inputs = ["text_chuban", "text_tanname"]
        for inp in inputs:
            if hasattr(self, inp):
                target = getattr(self, inp)
                if hasattr(target, "clear"):
                    target.clear()

        if hasattr(self, "tableWidget"):
            table = self.tableWidget
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

        today = QDate.currentDate()
        self.date_nouki_from.setDate(today)
        self.date_nouki_to.setDate(today)
        self.date_juchu_date_from.setDate(today.addMonths(-1))
        self.date_juchu_date_to.setDate(today)

        self.chk_nouki.setChecked(True)
        self.chk_juchu_date.setChecked(True)
        self.chk_juchu_date.setChecked(False)

    def on_nextButton_click(self):
        """「次へ」ボタン押下時"""
        if self.all_details_df is None or not self.grouped_keys:
            return
        self.current_group_idx += 1
        if self.current_group_idx >= len(self.grouped_keys):
            self.current_group_idx = 0
        self._display_current_group()

    def on_prevButton_click(self):
        """「前へ」ボタン押下時"""
        if self.all_details_df is None or not self.grouped_keys:
            return
        self.current_group_idx -= 1
        if self.current_group_idx < 0:
            self.current_group_idx = len(self.grouped_keys) - 1
        self._display_current_group()

    def _display_current_group(self):
        """現在選択されているインデックスの伝票情報を描画する"""
        if not self.grouped_keys or self.all_details_df is None:
            return

        if hasattr(self, "word_count"):
            self.word_count.setText(f"{self.current_group_idx + 1} / {len(self.grouped_keys)} 件")

        current_key = self.grouped_keys[self.current_group_idx]
        key_dendat, key_tyuban, key_nouki, key_toknm1, key_tancd = current_key

        cond_dendat = (self.all_details_df["JUH_DENDAT"] == key_dendat) | (pd.isna(self.all_details_df["JUH_DENDAT"]) & pd.isna(key_dendat))
        cond_tyuban = (self.all_details_df["JUM_TYUBAN"] == key_tyuban) | (pd.isna(self.all_details_df["JUM_TYUBAN"]) & pd.isna(key_tyuban))
        cond_nouki = (self.all_details_df["JUH_NOUKI"] == key_nouki) | (pd.isna(self.all_details_df["JUH_NOUKI"]) & pd.isna(key_nouki))
        cond_toknm1 = (self.all_details_df["JUH_TOKNM1"] == key_toknm1) | (pd.isna(self.all_details_df["JUH_TOKNM1"]) & pd.isna(key_toknm1))
        cond_tancd = (self.all_details_df["JUH_TANCD"] == key_tancd) | (pd.isna(self.all_details_df["JUH_TANCD"]) & pd.isna(key_tancd))

        df_sub = self.all_details_df[cond_dendat & cond_tyuban & cond_nouki & cond_toknm1 & cond_tancd]
        if df_sub.empty:
            return

        first_row = df_sub.iloc[0].to_dict()

        def format_to_date(val):
            if pd.isna(val) or str(val).strip() in ["", "nan", "NaT"]:
                return ""
            try:
                return pd.to_datetime(val).strftime("%Y/%m/%d")
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
            if hasattr(self, label_name):
                getattr(self, label_name).setText(val)

        if hasattr(self, "tableWidget"):
            table = self.tableWidget
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

    def close_window(self):
        """【共通関数呼び出し】親画面を表示させて自身を閉じる"""
        common_utils.handle_window_close(self, self.parent_menu, getattr(self, "parent_root", None))

    def closeEvent(self, event):
        """×ボタンクリック時の終了ロジック"""
        self.close_window()
        event.accept()


def create_cell_item_helper(val, is_numeric=False, align_center=False, is_header=False):
    """QTableWidgetItem を生成・装飾する共通ヘルパー関数"""
    text = str(val) if pd.notna(val) else ""
    if is_numeric:
        try:
            text = f"{int(float(val)):,}"
        except (ValueError, TypeError):
            text = "0" if text == "" else text

    item = QTableWidgetItem(text)
    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

    font = QFont()
    font.setBold(True)
    item.setFont(font)

    if is_header:
        item.setBackground(QColor("#94a3b8"))
        item.setForeground(QColor("#ffffff"))
    else:
        item.setBackground(QColor("#f1f5f9"))
        item.setData(12, QBrush(QColor("#94a3b8")))

    if align_center or is_header:
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    elif is_numeric:
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    else:
        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

    return item


def show_window(parent_root):
    """外部から呼び出すためのエントリー関数"""
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
