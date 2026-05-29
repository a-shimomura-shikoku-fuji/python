import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import common_utils

# PySide6の必要なクラスのみをインポート
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# 💡 ui_files フォルダ内の変換済み Python ファイルからクラスをインポート
from ui_files.menu_ui import Ui_MainMenuWindow

# 各子画面のクラスを別ファイルからインポート
from controllers.app_general_search import GeneralSearchWindow
from controllers.app_juchushokai import MyWindow as JuchuShokaiWindow
from controllers.app_urikake import UrikakeWindow
from controllers.app_nouhin import NouhinWindow

# Pythonに古い一時ファイル（.pyc）を作らせない設定
sys.dont_write_bytecode = True


class MainMenuWindow:
    """【親画面】業務支援メニュー（5つのカテゴリ）を制御するクラス"""

    def __init__(self):
        # 💡 QUiLoaderの代わりに、QMainWindowを作ってUi_MainWindowのデザインを適用
        self.main_window_instance = QMainWindow()
        self.ui = Ui_MainMenuWindow()
        self.ui.setupUi(self.main_window_instance)

        # 💡 ウィンドウ全体の操作は本体インスタンス（main_window_instance）に対して行う
        common_utils.set_common_window_icon(self.main_window_instance)

        # 2. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.main_window_instance.setWindowTitle("業務支援メニュー")
        self.main_window_instance.setFixedSize(self.main_window_instance.size())

        # 💡 【デザインの絶対保持】
        self.main_window_instance.setStyleSheet(self.main_window_instance.styleSheet())

        # =========================================================================
        # 🌟【最高峰の保守性：一括管理辞書】
        # =========================================================================
        self.child_systems_map = {
            "general_search": GeneralSearchWindow,   # 汎用検索
            "juchushokai": JuchuShokaiWindow,        # 受注照会
            "urikake": UrikakeWindow,                # 売掛金回収状況一覧
            "nouhin": NouhinWindow,                  # 納品書に基づく売上内訳
        }

        # 起動した子画面の多重（二重）起動を完璧にガードするためのメモリ管理用辞書
        self.active_windows = {}

        # =========================================================================
        # 💡 各ボタンのイベント登録（元のコードを完全に維持）
        # =========================================================================
        if hasattr(self.ui, "btn_general_search"):
            self.ui.btn_general_search.clicked.connect(lambda: self._open_child_system("general_search"))

        if hasattr(self.ui, "btn_juchushokai"):
            self.ui.btn_juchushokai.clicked.connect(lambda: self._open_child_system("juchushokai"))

        if hasattr(self.ui, "btn_urikake"):
            self.ui.btn_urikake.clicked.connect(lambda: self._open_child_system("urikake"))

        if hasattr(self.ui, "btn_nouhin"):
            self.ui.btn_nouhin.clicked.connect(lambda: self._open_child_system("nouhin"))

        # 2. 5つの部署ナビゲーションボタンのイベント登録 (ページインデックスと同期)
        self.ui.btn_kyotsu.clicked.connect(lambda: self._switch_department(0))      # 共通
        self.ui.btn_hinshitsu.clicked.connect(lambda: self._switch_department(1))   # 品質保証部
        self.ui.btn_eigyo.clicked.connect(lambda: self._switch_department(2))       # 営業技術部
        self.ui.btn_soumu.clicked.connect(lambda: self._switch_department(3))       # 総務部
        self.ui.btn_seizo.clicked.connect(lambda: self._switch_department(4))       # 製造部

        # 初期状態で「共通」のページを開く
        self._switch_department(0)

    def show(self):
        """ウィンドウを表示する"""
        self.main_window_instance.show()

    def _switch_department(self, index):
        """右側のQStackedWidgetと左ボタンのチェック状態を同期"""
        self.ui.stackedWidget.setCurrentIndex(index)
        self.ui.btn_kyotsu.setChecked(index == 0)
        self.ui.btn_hinshitsu.setChecked(index == 1)
        self.ui.btn_eigyo.setChecked(index == 2)
        self.ui.btn_soumu.setChecked(index == 3)
        self.ui.btn_seizo.setChecked(index == 4)

    def _open_child_system(self, system_key):
        """🌟【共通自動起動ロジック】辞書からクラスを読み出し、二重起動を完全にガードして呼び出す"""
        target_class = self.child_systems_map.get(system_key)
        if not target_class:
            return

        # すでに該当する子画面が立ち上がっており、かつ画面上に残っている場合
        current_win = self.active_windows.get(system_key)
        if current_win:
            win_ui = current_win.ui if hasattr(current_win, "ui") else current_win
            if hasattr(win_ui, "isVisible") and win_ui.isVisible():
                win_ui.raise_()
                win_ui.activateWindow()
                return

        # 💡 受注照会画面(MyWindow)の引数(parent_root, parent_menu)と、他画面(parent_menu)の差分を安全に吸収
        import inspect
        sig = inspect.signature(target_class.__init__)
        if "parent_root" in sig.parameters:
            new_win = target_class(parent_root=None, parent_menu=self)
        else:
            new_win = target_class(parent_menu=self)

        self.active_windows[system_key] = new_win
        new_win.show()

    def show_menu(self):
        """子画面が閉じられたときに、後ろにいたメニューを最前面に呼び出す"""
        self.main_window_instance.raise_()
        self.main_window_instance.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_window = MainMenuWindow()
    menu_window.show()
    sys.exit(app.exec())
