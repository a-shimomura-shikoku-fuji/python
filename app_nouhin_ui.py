# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_nouhin.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

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
"QLabel#label_target {\n"
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
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 30, 120, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #1e3a8a;")
        self.label_target = QLabel(self.centralwidget)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setGeometry(QRect(20, 60, 101, 21))
        self.label_target.setFont(font1)
        self.label_target.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_Target = QDateEdit(self.centralwidget)
        self.date_Target.setObjectName(u"date_Target")
        self.date_Target.setGeometry(QRect(120, 60, 111, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.date_Target.setFont(font2)
        self.date_Target.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_Target.setCalendarPopup(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 230, 431, 51))
        self.frame.setStyleSheet(u"background-color: #f1f5f9; \n"
"border: 1px solid #475569;\n"
"border-radius: 6px;")
        self.btn_back = QPushButton(self.frame)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 10, 51, 31))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setBold(True)
        self.btn_back.setFont(font3)
        self.btn_back.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")
        self.btn_excel = QPushButton(self.frame)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setGeometry(QRect(370, 10, 51, 31))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.btn_excel.setFont(font4)
        self.btn_excel.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: #ffffff !important; border: 1px solid #172554; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #2563eb; border-color: #60a5fa; }")
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(310, 10, 51, 31))
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569;; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(130, 10, 51, 31))
        self.pushButton_1.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 10, 51, 31))
        self.pushButton_3.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 10, 51, 31))
        self.pushButton_4.setStyleSheet(u"border: 1px solid #cbd5e1;")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 10, 51, 31))
        self.pushButton_2.setStyleSheet(u"border: 1px solid #cbd5e1;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7d0d\u54c1\u66f8\u306b\u57fa\u3065\u304f\u58f2\u4e0a\u5185\u8a33", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u6761\u4ef6\uff1e", None))
        self.label_target.setText(QCoreApplication.translate("MainWindow", u"\u5bfe\u8c61\u5e74\u6708", None))
        self.date_Target.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u529b", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.pushButton_1.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

