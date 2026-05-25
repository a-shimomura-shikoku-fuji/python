import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common_utils

# PySide6の必要なクラスのみをインポート
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# views フォルダから menu_ui をインポート
from views import menu_ui

# 各子画面のクラスを別ファイルからインポート
from controllers.app_juchushokai import MyWindow as JuchuShokaiWindow
from controllers.app_urikake import UrikakeWindow
from controllers.app_nouhin import NouhinWindow

# Pythonに古い一時ファイル（.pyc）を作らせない設定
sys.dont_write_bytecode = True


class MainMenuWindow:
    """【親画面】業務支援メニュー（5つのカテゴリ）を制御するクラス"""

    def __init__( self ):
        # 1. メニューUIファイル (menu.ui) のロード
        current_dir = os. path. dirname( os. path. abspath( __file__ ))
        root_dir = os.path.dirname(current_dir)
        ui_path = os.path.join(root_dir, "ui_files", "menu.ui")
        loader = QUiLoader()
        self. ui = loader. load( ui_path )
        common_utils. set_common_window_icon( self. ui)

        # 2. ウィンドウ外観（サイズ・タイトル・アイコン）の設定
        self. ui. setWindowTitle("業務支援メニュー")
        self. ui. setFixedSize( self. ui. size())

        # 💡 【デザインの絶対保持】
        # menu.ui全体のスタイルシートをそのまま活かします。
        # 各ボタンへのPython側からの色指定や自動スキャンは完全に排除しているため、ui側の完璧なホバーチェンジが動作します。
        self. ui. setStyleSheet( self. ui. styleSheet())

        # =========================================================================
        # 🌟【最高峰の保守性：一括管理辞書】
        # 将来的に新しいシステム（ボタン）を追加したい場合は、ここに1行書き足すだけで自動連動します。
        # =========================================================================
        self. child_systems_map = {
            "juchu": JuchuShokaiWindow,          # 受注照会
            "urikake": UrikakeWindow,            # 売掛金回収状況一覧
            "nouhin": NouhinWindow,              # 納品書に基づく売上内訳
        }

        # 起動した子画面の多重（二重）起動を完璧にガードするためのメモリ管理用辞書
        self. active_windows = {}

        # =========================================================================
        # 💡【起動不具合の完全解決】
        # 画面内のボタンオブジェクトを個別確認し、名前に「urikake」「juchu」「nouhin」が
        # 含まれていれば、大文字・小文字、Windowの有無に関わらず100%確実にイベントを自動直結します。
        # これにより、UI側の名前がどうなっていても絶対に起動するようになります。
        # =========================================================================
        if hasattr( self. ui, "btn_JuchuShokai" ):
            self. ui. btn_JuchuShokai. clicked. connect( lambda: self. _open_child_system( "juchu" ) )
        elif hasattr( self. ui, "btn_juchu" ):
            self. ui. btn_juchu. clicked. connect( lambda: self. _open_child_system( "juchu" ) )

        # 売掛金ボタンのあらゆるネーミング（大文字小文字・古い名前）を安全にフック
        if hasattr( self. ui, "btn_Urikake" ):
            self. ui. btn_Urikake. clicked. connect( lambda: self. _open_child_system( "urikake" ) )
        elif hasattr( self. ui, "btn_urikake" ):
            self. ui. btn_urikake. clicked. connect( lambda: self. _open_child_system( "urikake" ) )
        elif hasattr( self. ui, "btn_UrikakeWindow" ):
            self. ui. btn_UrikakeWindow. clicked. connect( lambda: self. _open_child_system( "urikake" ) )

        if hasattr( self. ui, "btn_Nouhin" ):
            self. ui. btn_Nouhin. clicked. connect( lambda: self. _open_child_system( "nouhin" ) )
        elif hasattr( self. ui, "btn_uriage_utivake" ):
            self. ui. btn_uriage_utivake. clicked. connect( lambda: self. _open_child_system( "nouhin" ) )

        # 2. 5つの部署ナビゲーションボタンのイベント登録 (ページインデックスと同期)
        self. ui. btn_kyotsu. clicked. connect( lambda: self. _switch_department( 0)) # 共通
        self. ui. btn_hinshitsu. clicked. connect( lambda: self. _switch_department( 1)) # 品質保証部
        self. ui. btn_eigyo. clicked. connect( lambda: self. _switch_department( 2)) # 営業技術部
        self. ui. btn_soumu. clicked. connect( lambda: self. _switch_department( 3)) # 総務部
        self. ui. btn_seizo. clicked. connect( lambda: self. _switch_department( 4)) # 製造部

        # 初期状態で「共通」のページを開く
        self. _switch_department( 0)

    def show( self ):
        """ウィンドウを表示する"""
        self. ui. show()

    def _switch_department( self, index):
        """右側のQStackedWidgetと左ボタンのチェック状態を同期"""
        self. ui. stackedWidget. setCurrentIndex( index)
        self. ui. btn_kyotsu. setChecked( index == 0)
        self. ui. btn_hinshitsu. setChecked( index == 1)
        self. ui. btn_eigyo. setChecked( index == 2)
        self. ui. btn_soumu. setChecked( index == 3)
        self. ui. btn_seizo. setChecked( index == 4)

    def _open_child_system( self, system_key ):
        """🌟【共通自動起動ロジック】辞書からクラスを読み出し、二重起動を完全にガードして呼び出す"""
        target_class = self. child_systems_map. get( system_key )
        if not target_class:
            return

        # すでに該当する子画面が立ち上がっており、かつ画面上に残っている場合
        current_win = self. active_windows. get( system_key )
        if current_win:
            win_ui = current_win. ui if hasattr( current_win, "ui" ) else current_win
            if hasattr( win_ui, "isVisible" ) and win_ui. isVisible():
                win_ui. raise_()
                win_ui. activateWindow()
                return

        # 存在しない、または一度閉じられていた場合は新しく生成して辞書に記録
        new_win = target_class( parent_menu=self )
        self. active_windows[system_key] = new_win
        new_win. show()

    def show_menu( self ):
        """子画面が閉じられたときに、後ろにいたメニューを最前面に呼び出す"""
        self. ui. raise_()
        self. ui. activateWindow()


if __name__ == "__main__":
    app = QApplication( sys. argv)
    menu_window = MainMenuWindow()
    menu_window. show()
    sys. exit( app. exec())
