# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_urikake_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_SubWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 300)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"/*  \u30a6\u30a4\u30f3\u30c9\u30a6\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QMainWindow {\n"
"    background-color: #f8fafc;\n"
"}\n"
"\n"
"/* \u30bf\u30a4\u30c8\u30eb\u30e9\u30d9\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"title_\"]  {\n"
"    color: #1e3a8a;\n"
"}\n"
"\n"
"/* \u5165\u529b\u9805\u76ee\u30e9\u30d9\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"label_\"]  {\n"
"    background-color: #64748b;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #64748b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u5165\u529b\u9805\u76ee\u8868\u793a\u30c7\u30fc\u30bf\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"data_\"]  {\n"
"    background-color: #f1f5f9;\n"
"    color: #334155;\n"
"    font-weight: bold;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"/* \u5165\u529b\u9805\u76ee\u30c6\u30ad\u30b9\u30c8\uff08QTextEdit\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QTextEdit {\n"
"    backgrou"
                        "nd-color: #ffffff;\n"
"    color: #0f172a;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"/* \u5165\u529b\u9805\u76ee\u65e5\u4ed8\uff08QDateEdit\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QDateEdit {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px 4px;\n"
"}\n"
"QDateEdit:focus {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"/* \u8868\u793a\u9805\u76ee\u30e9\u30d9\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"label_disp_\"]  {\n"
"    background-color: #94a3b8;\n"
"    color: #ffffff !important;\n"
"    font-weight: bold;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u30d5\u30ec\u30fc\u30e0\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QFrame#frame_btn {\n"
"    background-color: #f1f5f9; \n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#frame_search_r"
                        "esults {\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u901a\u5e38\u30dc\u30bf\u30f3\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton[objectName^=\"btn_exe_\"] {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #172554;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton[objectName^=\"btn_exe_\"]:hover {\n"
"    background-color: #2563eb;\n"
"    border-color: #60a5fa;\n"
"}\n"
"QPushButton[objectName^=\"btn_exe_\"]:pressed {\n"
"    background-color: #1d4ed8;\n"
"    border-color: #3b82f6;\n"
"    color: #eff6ff;\n"
"}\n"
"\n"
"/* \u623b\u308b\u30dc\u30bf\u30f3\u3001\u30af\u30ea\u30a2\u30dc\u30bf\u30f3\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton#btn_back, \n"
"QPushButton#btn_clear { \n"
"    background-color: #e2e8f0;\n"
"    color: #475569;\n"
"    font-weight: bold; \n"
"    border: 1px solid #475569;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton#btn_back:hover, \n"
"QPushButton#btn_clear:hover { \n"
""
                        "    background-color: #cbd5e1;\n"
"    color: #334155;            \n"
"    border: 1px solid #334155;\n"
"}\n"
"QPushButton#btn_back:pressed, \n"
"QPushButton#btn_clear:pressed { \n"
"    background-color: #94a3b8;\n"
"    color: #1e293b; \n"
"    border: 1px solid #1e293b;\n"
"}\n"
"\n"
"/* \u30c0\u30df\u30fc\u30dc\u30bf\u30f3\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton[objectName^=\"btn_dummy_\"] {\n"
"    background-color: #f1f5f9; \n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_tokcode = QLabel(self.centralwidget)
        self.label_tokcode.setObjectName(u"label_tokcode")
        self.label_tokcode.setGeometry(QRect(20, 60, 101, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_tokcode.setFont(font1)
        self.label_tokcode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setGeometry(QRect(20, 230, 441, 51))
        self.frame_btn.setStyleSheet(u"")
        self.btn_back = QPushButton(self.frame_btn)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 10, 51, 31))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setBold(True)
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"")
        self.btn_exe_change = QPushButton(self.frame_btn)
        self.btn_exe_change.setObjectName(u"btn_exe_change")
        self.btn_exe_change.setGeometry(QRect(380, 10, 51, 31))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_exe_change.setFont(font3)
        self.btn_exe_change.setStyleSheet(u"")
        self.btn_clear = QPushButton(self.frame_btn)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(320, 10, 51, 31))
        self.btn_clear.setFont(font2)
        self.btn_clear.setStyleSheet(u"")
        self.btn_dummy_2 = QPushButton(self.frame_btn)
        self.btn_dummy_2.setObjectName(u"btn_dummy_2")
        self.btn_dummy_2.setGeometry(QRect(140, 10, 51, 31))
        self.btn_dummy_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_2.setStyleSheet(u"")
        self.btn_dummy_3 = QPushButton(self.frame_btn)
        self.btn_dummy_3.setObjectName(u"btn_dummy_3")
        self.btn_dummy_3.setGeometry(QRect(200, 10, 51, 31))
        self.btn_dummy_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_3.setStyleSheet(u"")
        self.btn_dummy_4 = QPushButton(self.frame_btn)
        self.btn_dummy_4.setObjectName(u"btn_dummy_4")
        self.btn_dummy_4.setGeometry(QRect(260, 10, 51, 31))
        self.btn_dummy_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_4.setStyleSheet(u"")
        self.btn_dummy_1 = QPushButton(self.frame_btn)
        self.btn_dummy_1.setObjectName(u"btn_dummy_1")
        self.btn_dummy_1.setGeometry(QRect(80, 10, 51, 31))
        self.btn_dummy_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_1.setStyleSheet(u"")
        self.text_tokcode = QTextEdit(self.centralwidget)
        self.text_tokcode.setObjectName(u"text_tokcode")
        self.text_tokcode.setGeometry(QRect(120, 60, 71, 21))
        font4 = QFont()
        font4.setPointSize(10)
        self.text_tokcode.setFont(font4)
        self.text_tokcode.setStyleSheet(u"")
        self.text_tokcode.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.data_tokname = QLabel(self.centralwidget)
        self.data_tokname.setObjectName(u"data_tokname")
        self.data_tokname.setGeometry(QRect(190, 60, 271, 21))
        self.data_tokname.setFont(font1)
        self.data_tokname.setStyleSheet(u"")
        self.title_search_conditions = QLabel(self.centralwidget)
        self.title_search_conditions.setObjectName(u"title_search_conditions")
        self.title_search_conditions.setGeometry(QRect(30, 30, 81, 21))
        self.title_search_conditions.setFont(font1)
        self.title_search_conditions.setStyleSheet(u"")
        self.title_search_results = QLabel(self.centralwidget)
        self.title_search_results.setObjectName(u"title_search_results")
        self.title_search_results.setGeometry(QRect(30, 110, 81, 21))
        self.title_search_results.setFont(font1)
        self.title_search_results.setStyleSheet(u"")
        self.frame_search_results = QFrame(self.centralwidget)
        self.frame_search_results.setObjectName(u"frame_search_results")
        self.frame_search_results.setGeometry(QRect(20, 140, 441, 61))
        self.frame_search_results.setStyleSheet(u"")
        self.frame_search_results.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_search_results.setFrameShadow(QFrame.Shadow.Raised)
        self.text_order = QTextEdit(self.frame_search_results)
        self.text_order.setObjectName(u"text_order")
        self.text_order.setGeometry(QRect(120, 20, 71, 21))
        self.text_order.setFont(font4)
        self.text_order.setStyleSheet(u"")
        self.text_order.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_disp_order = QLabel(self.frame_search_results)
        self.label_disp_order.setObjectName(u"label_disp_order")
        self.label_disp_order.setGeometry(QRect(20, 20, 101, 21))
        self.label_disp_order.setFont(font1)
        self.label_disp_order.setStyleSheet(u"")
        self.label_disp_order.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chk_uriagezero = QCheckBox(self.frame_search_results)
        self.chk_uriagezero.setObjectName(u"chk_uriagezero")
        self.chk_uriagezero.setGeometry(QRect(210, 20, 211, 21))
        self.chk_uriagezero.setFont(font4)
        self.chk_uriagezero.setStyleSheet(u"border: none")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_search_results.raise_()
        self.label_tokcode.raise_()
        self.frame_btn.raise_()
        self.text_tokcode.raise_()
        self.data_tokname.raise_()
        self.title_search_conditions.raise_()
        self.title_search_results.raise_()
        QWidget.setTabOrder(self.text_tokcode, self.text_order)
        QWidget.setTabOrder(self.text_order, self.chk_uriagezero)
        QWidget.setTabOrder(self.chk_uriagezero, self.btn_back)
        QWidget.setTabOrder(self.btn_back, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.btn_exe_change)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u58f2\u639b\u91d1\u56de\u53ce\u72b6\u6cc1\u4e00\u89a7\uff08\u51fa\u529b\u8a2d\u5b9a\u5909\u66f4\uff09", None))
        self.label_tokcode.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u30b3\u30fc\u30c9", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_exe_change.setText(QCoreApplication.translate("MainWindow", u"\u5909\u66f4", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.btn_dummy_2.setText("")
        self.btn_dummy_3.setText("")
        self.btn_dummy_4.setText("")
        self.btn_dummy_1.setText("")
        self.data_tokname.setText("")
        self.title_search_conditions.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u6761\u4ef6\uff1e", None))
        self.title_search_results.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u7d50\u679c\uff1e", None))
        self.label_disp_order.setText(QCoreApplication.translate("MainWindow", u"\u8868\u793a\u9806", None))
        self.chk_uriagezero.setText(QCoreApplication.translate("MainWindow", u"\u58f2\u4e0a\u91d1\u984d\u304c0\u306e\u5834\u5408\u306f\u8868\u793a\u3057\u306a\u3044", None))
    # retranslateUi

