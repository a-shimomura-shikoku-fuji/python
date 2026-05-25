# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_general_search.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 700)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow { background-color: #f8fafc; }\n"
"QLabel[objectName^=\"label_\"] {\n"
"    background-color: #64748b;\n"
"    color: #ffffff !important;\n"
"    font-weight: bold;\n"
"    border: 1px solid #64748b;\n"
"    border-radius: 4px;\n"
"}\n"
"QLabel#label_title_cond, QLabel#label_title_result {\n"
"    background-color: transparent;\n"
"    color: #1e3a8a !important;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"QComboBox, QTextEdit, QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    color: #0f172a;\n"
"}\n"
"QComboBox:focus, QTextEdit:focus, QListWidget:focus {\n"
"    border: 1px solid #3b82f6;\n"
"    background-color: #f8fafc;\n"
"}\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #475569;\n"
"    border: 1px solid #475569;\n"
"    padding: 1px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_title_cond = QLabel(self.centralwidget)
        self.label_title_cond.setObjectName(u"label_title_cond")
        self.label_title_cond.setGeometry(QRect(30, 10, 180, 16))
        self.label_table_lbl = QLabel(self.centralwidget)
        self.label_table_lbl.setObjectName(u"label_table_lbl")
        self.label_table_lbl.setGeometry(QRect(20, 35, 101, 21))
        self.label_table_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cmb_table_name = QComboBox(self.centralwidget)
        self.cmb_table_name.setObjectName(u"cmb_table_name")
        self.cmb_table_name.setGeometry(QRect(125, 35, 220, 21))
        self.cmb_table_name.setEditable(True)
        self.label_col_lbl = QLabel(self.centralwidget)
        self.label_col_lbl.setObjectName(u"label_col_lbl")
        self.label_col_lbl.setGeometry(QRect(20, 65, 101, 21))
        self.label_col_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cmb_column_name = QComboBox(self.centralwidget)
        self.cmb_column_name.setObjectName(u"cmb_column_name")
        self.cmb_column_name.setGeometry(QRect(125, 65, 160, 21))
        self.cmb_operator = QComboBox(self.centralwidget)
        self.cmb_operator.setObjectName(u"cmb_operator")
        self.cmb_operator.setGeometry(QRect(290, 65, 110, 21))
        self.text_cond_value = QTextEdit(self.centralwidget)
        self.text_cond_value.setObjectName(u"text_cond_value")
        self.text_cond_value.setGeometry(QRect(405, 65, 200, 21))
        self.text_cond_value.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.btn_add_cond = QPushButton(self.centralwidget)
        self.btn_add_cond.setObjectName(u"btn_add_cond")
        self.btn_add_cond.setGeometry(QRect(610, 65, 50, 21))
        self.btn_add_cond.setStyleSheet(u"QPushButton { background-color: #2563eb; color: #ffffff !important; border-radius: 4px; font-weight: bold; } QPushButton:hover { background-color: #1d4ed8; }")
        self.label_list_lbl = QLabel(self.centralwidget)
        self.label_list_lbl.setObjectName(u"label_list_lbl")
        self.label_list_lbl.setGeometry(QRect(20, 95, 101, 50))
        self.label_list_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.listWidget_conds = QListWidget(self.centralwidget)
        self.listWidget_conds.setObjectName(u"listWidget_conds")
        self.listWidget_conds.setGeometry(QRect(125, 95, 480, 50))
        self.btn_del_cond = QPushButton(self.centralwidget)
        self.btn_del_cond.setObjectName(u"btn_del_cond")
        self.btn_del_cond.setGeometry(QRect(610, 95, 50, 25))
        self.btn_del_cond.setStyleSheet(u"QPushButton { background-color: #dc2626; color: #ffffff !important; border-radius: 4px; font-weight: bold; } QPushButton:hover { background-color: #b91c1c; }")
        self.label_keyword_lbl = QLabel(self.centralwidget)
        self.label_keyword_lbl.setObjectName(u"label_keyword_lbl")
        self.label_keyword_lbl.setGeometry(QRect(20, 155, 101, 21))
        self.label_keyword_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_keyword = QTextEdit(self.centralwidget)
        self.text_keyword.setObjectName(u"text_keyword")
        self.text_keyword.setGeometry(QRect(125, 155, 535, 21))
        self.text_keyword.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_title_result = QLabel(self.centralwidget)
        self.label_title_result.setObjectName(u"label_title_result")
        self.label_title_result.setGeometry(QRect(30, 190, 120, 16))
        self.label_Count = QLabel(self.centralwidget)
        self.label_Count.setObjectName(u"label_Count")
        self.label_Count.setGeometry(QRect(540, 190, 120, 16))
        self.label_Count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 215, 700, 300))
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 590, 700, 51))
        self.frame.setStyleSheet(u"background-color: #f1f5f9; border: 1px solid #475569; border-radius: 6px;")
        self.pushButton_ESC = QPushButton(self.frame)
        self.pushButton_ESC.setObjectName(u"pushButton_ESC")
        self.pushButton_ESC.setGeometry(QRect(10, 10, 51, 31))
        self.pushButton_ESC.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569; border-radius: 6px; font-weight: bold; } QPushButton:hover { background-color: #cbd5e1; }")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 10, 90, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton { background-color: #0d9488; color: #ffffff !important; border: 1px solid #0f766e; border-radius: 6px; font-weight: bold; } QPushButton:hover { background-color: #0cc5b3; }")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(210, 10, 10, 31))
        self.pushButton_1.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(520, 10, 51, 31))
        self.pushButton_9.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: #ffffff !important; border: 1px solid #172554; border-radius: 6px; font-weight: bold; } QPushButton:hover { background-color: #2563eb; border-color: #60a5fa; }")
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(580, 10, 51, 31))
        self.pushButton_10.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569; border-radius: 6px; font-weight: bold; } QPushButton:hover { background-color: #cbd5e1; }")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u30c7\u30fc\u30bf\u30d9\u30fc\u30b9\u6c4e\u7528\u30de\u30eb\u30c1\u8a73\u7d30\u691c\u7d22", None))
        self.label_title_cond.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u8907\u6570\u6761\u4ef6\u691c\u7d22\u8a2d\u5b9a\uff1e", None))
        self.label_table_lbl.setText(QCoreApplication.translate("MainWindow", u"\u5bfe\u8c61\u30c6\u30fc\u30d6\u30eb", None))
        self.label_col_lbl.setText(QCoreApplication.translate("MainWindow", u"\u6761\u4ef6\u306e\u898f\u5247", None))
        self.text_cond_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5024\u3092\u5165\u529b", None))
        self.btn_add_cond.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0", None))
        self.label_list_lbl.setText(QCoreApplication.translate("MainWindow", u"\u73fe\u5728\u306e\u6761\u4ef6\n"
"(AND\u7d50\u5408)", None))
        self.btn_del_cond.setText(QCoreApplication.translate("MainWindow", u"\u524a\u9664", None))
        self.label_keyword_lbl.setText(QCoreApplication.translate("MainWindow", u"\u7d50\u679c\u5185\u691c\u7d22", None))
        self.text_keyword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30b9\u30da\u30fc\u30b9\u533a\u5207\u308a\u3067\u3001\u62bd\u51fa\u3055\u308c\u305f\u30c7\u30fc\u30bf\u3092\u3055\u3089\u306b\u6a2a\u65ad\u7d5e\u308a\u8fbc\u307f\u3067\u304d\u307e\u3059", None))
        self.label_title_result.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u7167\u4f1a\u7d50\u679c\uff1e", None))
        self.label_Count.setText("")
        self.pushButton_ESC.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CSV\u51fa\u529b", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u7167\u4f1a", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
    # retranslateUi

