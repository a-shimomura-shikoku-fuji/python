# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_juchushokai.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QFrame, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 637)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow { background-color: #f8fafc; }\n"
"\n"
"/* \u9805\u76ee\u898b\u51fa\u3057\uff08\u30e9\u30d9\u30eb\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"label_1\"] {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff !important;\n"
"    font-weight: bold;\n"
"    border: 1px solid #172554;\n"
"    border-radius: 4px;\n"
"}\n"
"QLabel#label_2, QLabel#label_4, QLabel#label_6, QLabel#label_7 {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff !important;\n"
"    font-weight: bold;\n"
"    border: 1px solid #172554;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u95b2\u89a7\u5c02\u7528\uff08DB\u304b\u3089\u306e\u51fa\u529b\u7528\uff09\u30e9\u30d9\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel#label_toknm1, QLabel#label_nouki, QLabel#label_tyuban, QLabel#label_tanname, QLabel#label_dendat {\n"
"    background-color: #f1f5f9;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    color: #334155;\n"
"}\n"
"\n"
"/* \u5165\u529b\u30a8\u30ea\u30a2"
                        "\uff08QTextEdit / QDateEdit\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QTextEdit, QDateEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    color: #0f172a;\n"
"}\n"
"QTextEdit:focus, QDateEdit:focus {\n"
"    border: 1px solid #3b82f6;\n"
"    background-color: #f8fafc;\n"
"}\n"
"\n"
"/* \u30c6\u30fc\u30d6\u30eb\u5168\u4f53\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #cbd5e1;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 530, 651, 51))
        self.frame.setStyleSheet(u"background-color: #f1f5f9; \n"
"border: 1px solid #cbd5e1;\n"
"border-radius: 6px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_ESC = QPushButton(self.frame)
        self.pushButton_ESC.setObjectName(u"pushButton_ESC")
        self.pushButton_ESC.setGeometry(QRect(10, 10, 51, 31))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_ESC.setFont(font1)
        self.pushButton_ESC.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #cbd5e1; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 10, 51, 31))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: #ffffff !important; border: 1px solid #172554; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #2563eb; border-color: #60a5fa; }")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(170, 10, 51, 31))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: #ffffff !important; border: 1px solid #172554; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #2563eb; border-color: #60a5fa; }")
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(470, 10, 51, 31))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"QPushButton { background-color: #1e3a8a; color: #ffffff !important; border: 1px solid #172554; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #2563eb; border-color: #60a5fa; }")
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(530, 10, 51, 31))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setBold(True)
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #cbd5e1; border-radius: 6px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #cbd5e1; }")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(230, 10, 51, 31))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(290, 10, 51, 31))
        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(350, 10, 51, 31))
        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(410, 10, 51, 31))
        self.pushButton_17 = QPushButton(self.frame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(590, 10, 51, 31))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 280, 651, 241))
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.label_toknm1 = QLabel(self.centralwidget)
        self.label_toknm1.setObjectName(u"label_toknm1")
        self.label_toknm1.setGeometry(QRect(120, 180, 341, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_toknm1.setFont(font3)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 160, 101, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 180, 101, 21))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 200, 101, 71))
        self.label_16.setFont(font4)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(460, 180, 101, 21))
        self.label_15.setFont(font4)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(460, 160, 101, 21))
        self.label_13.setFont(font4)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_nouki = QLabel(self.centralwidget)
        self.label_nouki.setObjectName(u"label_nouki")
        self.label_nouki.setGeometry(QRect(560, 160, 111, 21))
        self.label_nouki.setFont(font3)
        self.label_tyuban = QLabel(self.centralwidget)
        self.label_tyuban.setObjectName(u"label_tyuban")
        self.label_tyuban.setGeometry(QRect(330, 160, 131, 21))
        self.label_tyuban.setFont(font3)
        self.label_tanname = QLabel(self.centralwidget)
        self.label_tanname.setObjectName(u"label_tanname")
        self.label_tanname.setGeometry(QRect(560, 180, 111, 21))
        self.label_tanname.setFont(font3)
        self.label_dendat = QLabel(self.centralwidget)
        self.label_dendat.setObjectName(u"label_dendat")
        self.label_dendat.setGeometry(QRect(120, 160, 111, 21))
        self.label_dendat.setFont(font3)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(230, 160, 101, 21))
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 101, 21))
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 130, 81, 16))
        self.label_8.setFont(font4)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 40, 21, 21))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 101, 21))
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 70, 21, 21))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(440, 40, 101, 21))
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(440, 70, 101, 21))
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_tyuban = QTextEdit(self.centralwidget)
        self.text_tyuban.setObjectName(u"text_tyuban")
        self.text_tyuban.setGeometry(QRect(540, 40, 131, 21))
        self.text_tyuban.setFont(font3)
        self.text_tyuban.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.date_Nouki_F = QDateEdit(self.centralwidget)
        self.date_Nouki_F.setObjectName(u"date_Nouki_F")
        self.date_Nouki_F.setGeometry(QRect(120, 40, 111, 21))
        self.date_Nouki_F.setFont(font3)
        self.date_Nouki_F.setCalendarPopup(True)
        self.date_Nouki_T = QDateEdit(self.centralwidget)
        self.date_Nouki_T.setObjectName(u"date_Nouki_T")
        self.date_Nouki_T.setGeometry(QRect(270, 40, 111, 21))
        self.date_Nouki_T.setFont(font3)
        self.date_Nouki_T.setCalendarPopup(True)
        self.date_Dendat_F = QDateEdit(self.centralwidget)
        self.date_Dendat_F.setObjectName(u"date_Dendat_F")
        self.date_Dendat_F.setGeometry(QRect(120, 70, 111, 21))
        self.date_Dendat_F.setFont(font3)
        self.date_Dendat_F.setCalendarPopup(True)
        self.date_Dendat_T = QDateEdit(self.centralwidget)
        self.date_Dendat_T.setObjectName(u"date_Dendat_T")
        self.date_Dendat_T.setGeometry(QRect(270, 70, 111, 21))
        self.date_Dendat_T.setFont(font3)
        self.date_Dendat_T.setCalendarPopup(True)
        self.label_Count = QLabel(self.centralwidget)
        self.label_Count.setObjectName(u"label_Count")
        self.label_Count.setGeometry(QRect(120, 130, 81, 16))
        self.label_Count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.text_tanname = QTextEdit(self.centralwidget)
        self.text_tanname.setObjectName(u"text_tanname")
        self.text_tanname.setGeometry(QRect(540, 70, 131, 21))
        self.text_tanname.setFont(font3)
        self.text_tanname.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_instructions = QTextEdit(self.centralwidget)
        self.text_instructions.setObjectName(u"text_instructions")
        self.text_instructions.setGeometry(QRect(120, 200, 551, 71))
        self.text_instructions.setFont(font3)
        self.text_instructions.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chk_Nouki = QCheckBox(self.centralwidget)
        self.chk_Nouki.setObjectName(u"chk_Nouki")
        self.chk_Nouki.setGeometry(QRect(390, 40, 21, 21))
        self.chk_Dendat = QCheckBox(self.centralwidget)
        self.chk_Dendat.setObjectName(u"chk_Dendat")
        self.chk_Dendat.setGeometry(QRect(390, 70, 21, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 10, 81, 16))
        self.label_9.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u7167\u4f1a", None))
        self.pushButton_ESC.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u524d\u3078", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6b21\u3078", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u7167\u4f1a", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.pushButton_1.setText("")
        self.pushButton_4.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u756a\u53f7", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u540d", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u30b5\u30a4\u30ba", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf\u660e\u7d30", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u5148\u4ed5\u69d8\u66f8No", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u3057\u3044\u5217", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u5099\u8003", None))
        self.label_toknm1.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u65e5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6307\u793a\u4e8b\u9805", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u62c5\u5f53\u8005", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7d0d\u671f", None))
        self.label_nouki.setText("")
        self.label_tyuban.setText("")
        self.label_tanname.setText("")
        self.label_dendat.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u6ce8\u756a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7d0d\u671f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u7167\u4f1a\u7d50\u679c\uff1e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uff5e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u65e5", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uff5e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u6ce8\u756a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u62c5\u5f53\u8005", None))
        self.label_Count.setText("")
        self.chk_Nouki.setText("")
        self.chk_Dendat.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u6761\u4ef6\uff1e", None))
    # retranslateUi

