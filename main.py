import sys
import os

# 一番最初にルートパスを通す
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication
from controllers.menu import MainMenuWindow  # クラス名は実際の menu.py に合わせてください

def main():
    app = QApplication(sys.argv)
    window = MainMenuWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
