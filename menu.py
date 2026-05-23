import os
import sys
import common_utils

# PySide6の必要なクラスのみをインポート
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

# 各子画面のクラスを別ファイルからインポート
from app_juchushokai import MyWindow as JuchuShokaiWindow
from app_urikake import UrikakeWindow
from app_nouhin import NouhinWindow

class MainMenuWindow:
    """【親画面】業務支援メニュー（5つのカテゴリ）を制御するクラス"""
    def __init__(self):
        # 1. メニューUIファイル (menu.ui) のロード
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "menu.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)

        common_utils.set_common_window_icon(self.ui)

        # 2. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self.ui.setWindowTitle("業務支援メニュー")

        # 💡 強制的にキャッシュを破壊してスタイルシートを適用
        self.ui.setStyleSheet(self.ui.styleSheet())

        # ==========================================================
        # ★【スタイルシート】通常時とホバー・フォーカス時の挙動を定義
        # ==========================================================
        btn_style = """
            QPushButton {
                color: #ffffff !important; 
                background-color: #1e3a8a; 
                border: 1px solid #172554; 
                border-radius: 6px; 
                font-weight: bold;
            }
            QPushButton:hover, QPushButton:focus {
                background-color: #2563eb;    /* ホバー・フォーカス時に明るい青へ変化 */
                border-color: #60a5fa;        /* 枠線を水色へ変化 */
            }
        """

        # 各ボタンオブジェクトが存在する場合にスタイルシートを適用
        if hasattr(self.ui, "btn_juchu"): self.ui.btn_juchu.setStyleSheet(btn_style)
        if hasattr(self.ui, "btn_urikake"): self.ui.btn_urikake.setStyleSheet(btn_style)
        if hasattr(self.ui, "btn_uriage_utivake"): self.ui.btn_uriage_utivake.setStyleSheet(btn_style)

        # ウィンドウの固定サイズ設定
        self.ui.setFixedSize(self.ui.size())

        # 2. 5つの部署ナビゲーションボタンのイベント登録 (ページインデックスと同期)
        self.ui.btn_common.clicked.connect(lambda: self._switch_department(0)) # 共通
        self.ui.btn_qa.clicked.connect(lambda: self._switch_department(1))     # 品質保証部
        self.ui.btn_sales.clicked.connect(lambda: self._switch_department(2))  # 営業技術部
        self.ui.btn_admin.clicked.connect(lambda: self._switch_department(3))  # 総務部
        self.ui.btn_factory.clicked.connect(lambda: self._switch_department(4)) # 製造部

        # ==========================================================
        # ★【追加実装】各ボタンのクリックイベントと起動処理を登録
        # ==========================================================
        # 営業技術部ページ内などの各システムボタンに処理を紐付け
        if hasattr(self.ui, "btn_juchu"):
            self.ui.btn_juchu.clicked.connect(self._open_juchu_shokai)
            
        if hasattr(self.ui, "btn_urikake"):
            self.ui.btn_urikake.clicked.connect(self._open_urikake)
            
        if hasattr(self.ui, "btn_uriage_utivake"):
            self.ui.btn_uriage_utivake.clicked.connect(self._open_nouhin)

        # 初期状態で「共通」のページを開く
        self._switch_department(0)
        self.child_window = None

    def show(self):
        """ウィンドウを表示する"""
        self.ui.show()

    def _switch_department(self, index):
        """右側のQStackedWidgetと左ボタンのチェック状態を同期"""
        self.ui.stackedWidget.setCurrentIndex(index)
        self.ui.btn_common.setChecked(index == 0)
        self.ui.btn_qa.setChecked(index == 1)
        self.ui.btn_sales.setChecked(index == 2)
        self.ui.btn_admin.setChecked(index == 3)
        self.ui.btn_factory.setChecked(index == 4)

    # ==========================================================
    # ★ 各子画面の起動処理（メニューを隠さず、連携して立ち上げる）
    # ==========================================================
    def _open_juchu_shokai(self):
        """受注照会を起動"""
        self.child_window = JuchuShokaiWindow(parent_menu=self)
        self.child_window.show()

    def _open_urikake(self):
        """売掛金回収状況一覧を起動"""
        self.child_window = UrikakeWindow(parent_menu=self)
        self.child_window.show()

    def _open_nouhin(self):
        """納品書に基づく売上内訳を起動"""
        self.child_window = NouhinWindow(parent_menu=self)
        self.child_window.show()

    def show_menu(self):
        """子画面が閉じられたときに、後ろにいたメニューを最前面に呼び出す"""
        self.ui.raise_()
        self.ui.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_window = MainMenuWindow()
    menu_window.show()
    sys.exit(app.exec())
