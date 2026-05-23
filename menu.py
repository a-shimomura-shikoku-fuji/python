import os
import sys

# PySide6の必要なクラスのみをインポート
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

# 別ファイルになっている受注照会クラスをインポート
from app_juchushokai import MyWindow as JuchuShokaiWindow


class MainMenuWindow:
    """【親画面】業務支援メニュー（5つのカテゴリ）を制御するクラス"""

    def __init__(self):
        # 1. メニューUIファイル (menu.ui) のロード
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "menu.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)

        # 💡 元のコードと100%同じデザイン適用ロジック（白文字ネイビー）に完全復元
        self.ui.setStyleSheet(self.ui.styleSheet())
        btn_style = "color: #ffffff !important; background-color: #1e3a8a; border: 1px solid #172554; border-radius: 6px; font-weight: bold;"
        
        if hasattr(self.ui, "btn_juchu"): 
            self.ui.btn_juchu.setStyleSheet(btn_style)
        if hasattr(self.ui, "btn_urikake"): 
            self.ui.btn_urikake.setStyleSheet(btn_style)
        if hasattr(self.ui, "btn_uriage_utivake"): 
            self.ui.btn_uriage_utivake.setStyleSheet(btn_style)

        # ウィンドウの固定サイズ設定
        self.ui.setFixedSize(self.ui.size())

        # 2. 5つの部署ナビゲーションボタンのイベント登録 (元の確実な lambda 制御に完全復元)
        self.ui.btn_common.clicked.connect(lambda: self._switch_department(0)) # 共通
        self.ui.btn_qa.clicked.connect(lambda: self._switch_department(1))     # 品質保証部
        self.ui.btn_sales.clicked.connect(lambda: self._switch_department(2))  # 営業技術部
        self.ui.btn_admin.clicked.connect(lambda: self._switch_department(3))  # 総務部
        self.ui.btn_factory.clicked.connect(lambda: self._switch_department(4)) # 製造部

        # 3. 営業技術部ページ内の「受注照会システム」ボタンに処理を登録
        self.ui.btn_juchu.clicked.connect(self._open_juchu_shokai)

        # 初期状態で「共通」のページを開く
        self._switch_department(0)
        self.child_window = None
    def show(self):
        """ウィンドウを表示する"""
        self.ui.show()

    def _switch_department(self, index):
        """【完全復元】右側のQStackedWidgetと左ボタンのチェック状態を同期"""
        self.ui.stackedWidget.setCurrentIndex(index)
        self.ui.btn_common.setChecked(index == 0)
        self.ui.btn_qa.setChecked(index == 1)
        self.ui.btn_sales.setChecked(index == 2)
        self.ui.btn_admin.setChecked(index == 3)
        self.ui.btn_factory.setChecked(index == 4)

    def _open_juchu_shokai(self):
        """【安全ガード追加】メニューを一切隠さず、子画面の二重起動のみを確実に防止する"""
        # すでに子画面が開かれており、画面上に目視できる場合は、新しく開かずに最前面へ呼び出す
        if self.child_window and hasattr(self.child_window, "ui") and self.child_window.ui.isVisible():
            self.child_window.ui.raise_()
            self.child_window.ui.activateWindow()
            return

        # 受注照会ウィンドウクラスを呼び出し（自分自身をparent_menuとして渡す）
        self.child_window = JuchuShokaiWindow(parent_menu=self)
        self.child_window.show()

    def show_menu(self):
        """【完全復元】子画面が閉じられたときに、後ろにいたメニューを最前面に呼び出す"""
        self.ui.raise_()
        self.ui.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_window = MainMenuWindow()
    menu_window.show()
    sys.exit(app.exec())
