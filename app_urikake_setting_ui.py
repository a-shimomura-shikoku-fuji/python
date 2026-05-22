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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 300)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow { background-color: #f8fafc; }\n"
"\n"
"QLabel#label_1{\n"
"    background-color: #64748b;\n"
"    color: #ffffff !important;\n"
"    font-weight: bold;\n"
"    border: 1px solid #64748b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u901a\u5e38\u30e9\u30d9\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel {\n"
"    color: #334155;\n"
"}\n"
"\n"
"/* \u65e5\u4ed8\u5165\u529b\u30a8\u30ea\u30a2\uff08QDateEdit\uff09\u306e\u30b9\u30bf\u30a4\u30eb\u3092\u6700\u9069\u5316 */\n"
"QDateEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px 4px;\n"
"    color: #0f172a;\n"
"}\n"
"QDateEdit:focus {\n"
"    border: 1px solid #3b82f6;\n"
"    background-color: #f8fafc;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 60, 101, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 230, 441, 51))
        self.frame.setStyleSheet(u"background-color: #f1f5f9; \n"
"border: 1px solid #475569;\n"
"border-radius: 6px;")
        self.btn_back = QPushButton(self.frame)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 10, 51, 31))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setBold(True)
        self.btn_back.setFont(font2)
        self.btn_back.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")
        self.btn_excute = QPushButton(self.frame)
        self.btn_excute.setObjectName(u"btn_excute")
        self.btn_excute.setGeometry(QRect(380, 10, 51, 31))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_excute.setFont(font3)
        self.btn_excute.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: #ffffff !important; border: 1px solid #172554; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #2563eb; border-color: #60a5fa; }")
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(320, 10, 51, 31))
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569;; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(140, 10, 51, 31))
        self.pushButton_1.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 10, 51, 31))
        self.pushButton_3.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(260, 10, 51, 31))
        self.pushButton_4.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 10, 51, 31))
        self.pushButton_2.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.text_tokcd = QTextEdit(self.centralwidget)
        self.text_tokcd.setObjectName(u"text_tokcd")
        self.text_tokcd.setGeometry(QRect(120, 60, 71, 21))
        font4 = QFont()
        font4.setPointSize(10)
        self.text_tokcd.setFont(font4)
        self.text_tokcd.setStyleSheet(u"background-color: #ffffff;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    color: #0f172a;\n"
"")
        self.text_tokcd.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_tokname = QLabel(self.centralwidget)
        self.label_tokname.setObjectName(u"label_tokname")
        self.label_tokname.setGeometry(QRect(190, 60, 271, 21))
        self.label_tokname.setFont(font1)
        self.label_tokname.setStyleSheet(u" background-color: #f1f5f9;\n"
"    font-weight: bold;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    color: #334155;\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 30, 81, 21))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #1e3a8a;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 110, 81, 21))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: #1e3a8a;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 140, 441, 61))
        self.frame_2.setStyleSheet(u"border: 1px solid #475569;\n"
"border-radius: 6px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.chk_uriagezero = QCheckBox(self.frame_2)
        self.chk_uriagezero.setObjectName(u"chk_uriagezero")
        self.chk_uriagezero.setGeometry(QRect(210, 20, 211, 21))
        self.chk_uriagezero.setFont(font4)
        self.text_sort = QTextEdit(self.frame_2)
        self.text_sort.setObjectName(u"text_sort")
        self.text_sort.setGeometry(QRect(120, 20, 71, 21))
        self.text_sort.setFont(font4)
        self.text_sort.setStyleSheet(u"background-color: #ffffff;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    color: #0f172a;\n"
"")
        self.text_sort.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 20, 101, 21))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"  background-color: #94a3b8;\n"
"    color: #ffffff !important;\n"
"    font-weight: bold;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 4px;\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.label_1.raise_()
        self.frame.raise_()
        self.text_tokcd.raise_()
        self.label_tokname.raise_()
        self.label_8.raise_()
        self.label_9.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u58f2\u639b\u91d1\u56de\u53ce\u72b6\u6cc1\u4e00\u89a7\uff08\u51fa\u529b\u8a2d\u5b9a\u5909\u66f4\uff09", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u30b3\u30fc\u30c9", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_excute.setText(QCoreApplication.translate("MainWindow", u"\u5909\u66f4", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.pushButton_1.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.label_tokname.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u6761\u4ef6\uff1e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u7d50\u679c\uff1e", None))
        self.chk_uriagezero.setText(QCoreApplication.translate("MainWindow", u"\u58f2\u4e0a\u91d1\u984d\u304c0\u306e\u5834\u5408\u306f\u8868\u793a\u3057\u306a\u3044", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8868\u793a\u9806", None))
    # retranslateUi

