# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_urikake.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 300)
        MainWindow.setMinimumSize(QSize(480, 300))
        MainWindow.setMaximumSize(QSize(481, 300))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"/*  \u30a6\u30a4\u30f3\u30c9\u30a6\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QMainWindow {\n"
"    background-color: #e2e8f0;\n"
"}\n"
"\n"
"/* \u30e9\u30d9\u30eb\uff1a\u30bf\u30a4\u30c8\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"title_\"]  {\n"
"    color: #1e3a8a;\n"
"}\n"
"\n"
"/* \u30e9\u30d9\u30eb\uff1a\u5165\u529b\u9805\u76ee\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"label_\"]  {\n"
"    background-color: #64748b;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #64748b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u5165\u529b\u9805\u76ee\uff1a\u65e5\u4ed8\uff08QDateEdit\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
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
"/*\u30d5\u30ec\u30fc\u30e0\u306e\u30b9\u30bf\u30a4\u30eb */\n"
""
                        "QFrame#frame_btn {\n"
"    background-color: #cbd5e1; \n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u30dc\u30bf\u30f3\uff1a\u901a\u5e38\u306e\u30b9\u30bf\u30a4\u30eb */\n"
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
"/* \u30dc\u30bf\u30f3\uff1a\u623b\u308b\u3001\u30af\u30ea\u30a2\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton#btn_back, \n"
"QPushButton#btn_clear { \n"
"    background-color: #e2e8f0;\n"
"    color: #475569;\n"
"    font-weight: bold; \n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton#btn_back:hover, "
                        "\n"
"QPushButton#btn_clear:hover { \n"
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
"/* \u30dc\u30bf\u30f3\uff1a\u30c0\u30df\u30fc\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton[objectName^=\"btn_dummy_\"] {\n"
"    background-color: #f1f5f9; \n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 40, 25, 20)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(430, 51))
        self.widget.setMaximumSize(QSize(430, 51))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_search_conditions = QLabel(self.widget)
        self.title_search_conditions.setObjectName(u"title_search_conditions")
        self.title_search_conditions.setMinimumSize(QSize(101, 21))
        self.title_search_conditions.setMaximumSize(QSize(101, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.title_search_conditions.setFont(font1)
        self.title_search_conditions.setStyleSheet(u"")

        self.gridLayout.addWidget(self.title_search_conditions, 0, 0, 1, 2)

        self.label_target_year_month = QLabel(self.widget)
        self.label_target_year_month.setObjectName(u"label_target_year_month")
        self.label_target_year_month.setMinimumSize(QSize(101, 21))
        self.label_target_year_month.setMaximumSize(QSize(101, 21))
        self.label_target_year_month.setFont(font1)
        self.label_target_year_month.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_target_year_month, 1, 0, 1, 1)

        self.date_target_year_month = QDateEdit(self.widget)
        self.date_target_year_month.setObjectName(u"date_target_year_month")
        self.date_target_year_month.setMinimumSize(QSize(101, 21))
        self.date_target_year_month.setMaximumSize(QSize(101, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.date_target_year_month.setFont(font2)
        self.date_target_year_month.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_target_year_month.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_target_year_month, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(427, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(430, 51))
        self.frame_btn.setMaximumSize(QSize(430, 51))
        self.frame_btn.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.frame_btn)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.btn_back = QPushButton(self.frame_btn)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(51, 31))
        self.btn_back.setMaximumSize(QSize(51, 31))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setBold(True)
        self.btn_back.setFont(font3)
        self.btn_back.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_dummy_1 = QPushButton(self.frame_btn)
        self.btn_dummy_1.setObjectName(u"btn_dummy_1")
        self.btn_dummy_1.setMinimumSize(QSize(51, 31))
        self.btn_dummy_1.setMaximumSize(QSize(51, 31))
        self.btn_dummy_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_1.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_dummy_1)

        self.btn_dummy_2 = QPushButton(self.frame_btn)
        self.btn_dummy_2.setObjectName(u"btn_dummy_2")
        self.btn_dummy_2.setMinimumSize(QSize(51, 31))
        self.btn_dummy_2.setMaximumSize(QSize(51, 31))
        self.btn_dummy_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_2.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_dummy_2)

        self.btn_dummy_3 = QPushButton(self.frame_btn)
        self.btn_dummy_3.setObjectName(u"btn_dummy_3")
        self.btn_dummy_3.setMinimumSize(QSize(51, 31))
        self.btn_dummy_3.setMaximumSize(QSize(51, 31))
        self.btn_dummy_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_3.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_dummy_3)

        self.btn_exe_setting = QPushButton(self.frame_btn)
        self.btn_exe_setting.setObjectName(u"btn_exe_setting")
        self.btn_exe_setting.setMinimumSize(QSize(51, 31))
        self.btn_exe_setting.setMaximumSize(QSize(51, 31))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.btn_exe_setting.setFont(font4)
        self.btn_exe_setting.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_exe_setting)

        self.btn_clear = QPushButton(self.frame_btn)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(51, 31))
        self.btn_clear.setMaximumSize(QSize(51, 31))
        self.btn_clear.setFont(font3)
        self.btn_clear.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_clear)

        self.btn_exe_output = QPushButton(self.frame_btn)
        self.btn_exe_output.setObjectName(u"btn_exe_output")
        self.btn_exe_output.setMinimumSize(QSize(51, 31))
        self.btn_exe_output.setMaximumSize(QSize(51, 31))
        self.btn_exe_output.setFont(font4)
        self.btn_exe_output.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_exe_output)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.date_target_year_month, self.btn_back)
        QWidget.setTabOrder(self.btn_back, self.btn_exe_setting)
        QWidget.setTabOrder(self.btn_exe_setting, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.btn_exe_output)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u58f2\u639b\u91d1\u56de\u53ce\u72b6\u6cc1\u4e00\u89a7", None))
        self.title_search_conditions.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u62bd\u51fa\u6761\u4ef6\uff1e", None))
        self.label_target_year_month.setText(QCoreApplication.translate("MainWindow", u"\u5bfe\u8c61\u5e74\u6708", None))
        self.date_target_year_month.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_dummy_1.setText("")
        self.btn_dummy_2.setText("")
        self.btn_dummy_3.setText("")
        self.btn_exe_setting.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9a", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.btn_exe_output.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u529b", None))
    # retranslateUi

