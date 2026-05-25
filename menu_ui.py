# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        if not MainMenuWindow.objectName():
            MainMenuWindow.setObjectName(u"MainMenuWindow")
        MainMenuWindow.resize(750, 480)
        MainMenuWindow.setStyleSheet(u"QMainWindow { background-color: #f8fafc; }\n"
"QFrame#Sidebar { background-color: #0f172a; }\n"
"\n"
"/* \U00005de6\U00005074\U000030ca\U000030d3\U000030b2\U000030fc\U000030b7\U000030e7\U000030f3\U000030dc\U000030bf\U000030f3\U0000ff08\U0000901a\U00005e38\U00006642\U0000ff09 */\n"
"QFrame#Sidebar QPushButton {\n"
"    color: #cbd5e1; \n"
"    background-color: transparent; \n"
"    text-align: left;\n"
"    padding-left: 14px; \n"
"    /* OS\U00006a19\U00006e96\U0000306e\U00007acb\U00004f53\U000067a0\U00003084\U000080cc\U0000666f\U00003092\U00005b8c\U00005168\U0000306b\U000030b7\U000030e3\U000030c3\U000030c8\U000030a2\U000030a6\U000030c8\U00003059\U0000308b\U0000305f\U00003081\U000030011px\U0000306e\U0000900f\U0000660e\U0000306a\U00007dda\U00003092\U0000660e\U0000793a\U00003057\U0000307e\U00003059 */\n"
"    border: 1px solid transparent; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \U0001f4a1 \U00003010\U00004fee\U00006b63\U00007b87\U00006240\U00003011\U000030db\U000030d0\U000030fc\U00006642\U0000306f\U000080cc"
                        "\U0000666f\U00008272\U00003092\U0000900f\U0000660e\U0000306a\U0000307e\U0000307e\U00003068\U00003057\U00003001\U00006307\U00005b9a\U00003057\U0000305f1\U0000672c\U0000306e\U000067a0\U00007dda\U0000ff08#1e293b\U0000ff09\U0000306e\U0000307f\U00003092\U00007f8e\U00003057\U0000304f\U000063cf\U0000753b\U00003057\U0000307e\U00003059 */\n"
"QFrame#Sidebar QPushButton:hover { \n"
"    color: #ffffff; \n"
"    background-color: transparent; \n"
"    border: 1px solid #1e293b;     \n"
"}\n"
"\n"
"/* \U0001f4a1 Tab\U000030ad\U000030fc\U00003067\U00009078\U0000629e\U00003055\U0000308c\U0000305f\U00006642\U0000ff08\U000030d5\U000030a9\U000030fc\U000030ab\U000030b9\U00006642\U0000ff09\U00003082\U00003001OS\U0000306e\U000067a0\U00003068\U000091cd\U0000306a\U00003089\U0000306a\U00003044\U00003088\U00003046\U00009752\U000030441\U0000672c\U0000306e\U000067a0\U00007dda\U00003067\U000030b9\U000030de\U000030fc\U000030c8\U0000306b\U00008868\U000073fe */\n"
"QFrame#Sidebar QPushButton:focus { \n"
"    color: #ffffff; \n"
"    backgr"
                        "ound-color: transparent; \n"
"    border: 1px solid #2563eb;     \n"
"}\n"
"\n"
"/* \U00005de6\U00005074\U000030ca\U000030d3\U000030b2\U000030fc\U000030b7\U000030e7\U000030f3\U000030dc\U000030bf\U000030f3\U0000ff08\U00009078\U0000629e\U000030fb\U000030c1\U000030a7\U000030c3\U000030af\U00003055\U0000308c\U0000305f\U000030a2\U000030af\U000030c6\U000030a3\U000030d6\U000072b6\U0000614b\U0000ff09 */\n"
"QFrame#Sidebar QPushButton:checked { \n"
"    color: #ffffff; \n"
"    background-color: #2563eb; \n"
"    border: 1px solid #2563eb; \n"
"    font-weight: bold; \n"
"}\n"
"/* \U000030c1\U000030a7\U000030c3\U000030af\U00003055\U0000308c\U00003066\U00003044\U0000308b\U000030dc\U000030bf\U000030f3\U0000306e\U00004e0a\U0000306b\U000030de\U000030a6\U000030b9\U0000304c\U00004e57\U00003063\U0000305f\U00006642\U0000306f\U00003001\U00009752\U00008272\U0000306e\U000080cc\U0000666f\U00003092\U000030ad\U000030fc\U000030d7\U00003055\U0000305b\U0000307e\U00003059 */\n"
"QFrame#Sidebar QPushButton:checked:hover {\n"
"    backgrou"
                        "nd-color: #2563eb;\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"/* =========================================================================\n"
"   \U0001f31f\U00003010\U00006700\U00009ad8\U00005cf0\U0000306e\U00004fdd\U00005b88\U00006027\U0000ff1a\U000053f3\U00005074\U0000696d\U000052d9\U00006a5f\U000080fd\U000030dc\U000030bf\U000030f3\U0000306e\U00004e00\U000062ec\U000081ea\U000052d5\U00005b9a\U00007fa9\U00003011\n"
"   \U00007279\U00005b9a\U0000306e\U000030aa\U000030d6\U000030b8\U000030a7\U000030af\U000030c8\U0000540d\U0000ff08#\U0000ff09\U00003092\U00007121\U0000304f\U00003057\U00003001QStackedWidget\U0000306e\U00004e2d\U0000306b\U00003042\U0000308b\U000030dc\U000030bf\U000030f3\U0000ff08\U000030af\U000030e9\U000030b9\U0000ff09\U00003068\U00003057\U00003066\U00005b9a\U00007fa9\U00003057\U0000307e\U00003059\U00003002\n"
"   \U00003053\U0000308c\U0000306b\U00003088\U0000308a\U00003001\U00005c06\U00006765\U000065b0\U00003057\U00003044\U000030dc\U000030bf\U000030f3\U00003092\U00005897\U00003084\U00003057\U0000305f"
                        "\U0000969b\U00003082QSS\U000030921\U0000884c\U00003082\U000076f4\U00003055\U0000305a\U0000306b\U00003053\U0000306e\U00006d17\U00007df4\U00003055\U0000308c\U0000305f\U000030c7\U000030b6\U000030a4\U000030f3\U0000304c\U000081ea\U000052d5\U00009069\U00007528\U00003055\U0000308c\U0000307e\U00003059\U00003002\n"
"   ========================================================================= */\n"
"QStackedWidget QPushButton {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff;\n"
"    border-radius: 6px;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    border: 1px solid #172554;\n"
"}\n"
"QStackedWidget QPushButton:hover, QStackedWidget QPushButton:focus {\n"
"    background-color: #2563eb;\n"
"    color: #ffffff;\n"
"    border: 1px solid #60a5fa;\n"
"}\n"
"QStackedWidget QPushButton:disabled {\n"
"    background-color: #f1f5f9;\n"
"    color: #94a3b8;\n"
"    border: 1px solid #e2e8f0;\n"
"}\n"
"")
        self.centralWidget = QWidget(MainMenuWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout_Main = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_Main.setSpacing(0)
        self.horizontalLayout_Main.setObjectName(u"horizontalLayout_Main")
        self.horizontalLayout_Main.setContentsMargins(0, 0, 0, 0)
        self.Sidebar = QFrame(self.centralWidget)
        self.Sidebar.setObjectName(u"Sidebar")
        self.Sidebar.setMinimumSize(QSize(180, 0))
        self.Sidebar.setMaximumSize(QSize(180, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.Sidebar.setFont(font)
        self.verticalLayout_Sidebar = QVBoxLayout(self.Sidebar)
        self.verticalLayout_Sidebar.setSpacing(8)
        self.verticalLayout_Sidebar.setObjectName(u"verticalLayout_Sidebar")
        self.verticalLayout_Sidebar.setContentsMargins(10, 20, 10, 20)
        self.title_label = QLabel(self.Sidebar)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamilies([u"Meiryo"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: #ffffff; margin-bottom: 15px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_Sidebar.addWidget(self.title_label)

        self.btn_kyotsu = QPushButton(self.Sidebar)
        self.btn_kyotsu.setObjectName(u"btn_kyotsu")
        self.btn_kyotsu.setMinimumSize(QSize(0, 42))
        font2 = QFont()
        font2.setFamilies([u"Meiryo"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.btn_kyotsu.setFont(font2)
        self.btn_kyotsu.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_kyotsu)

        self.btn_hinshitsu = QPushButton(self.Sidebar)
        self.btn_hinshitsu.setObjectName(u"btn_hinshitsu")
        self.btn_hinshitsu.setMinimumSize(QSize(0, 42))
        self.btn_hinshitsu.setFont(font2)
        self.btn_hinshitsu.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_hinshitsu)

        self.btn_eigyo = QPushButton(self.Sidebar)
        self.btn_eigyo.setObjectName(u"btn_eigyo")
        self.btn_eigyo.setMinimumSize(QSize(0, 42))
        self.btn_eigyo.setFont(font2)
        self.btn_eigyo.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_eigyo)

        self.btn_soumu = QPushButton(self.Sidebar)
        self.btn_soumu.setObjectName(u"btn_soumu")
        self.btn_soumu.setMinimumSize(QSize(0, 42))
        self.btn_soumu.setFont(font2)
        self.btn_soumu.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_soumu)

        self.btn_seizo = QPushButton(self.Sidebar)
        self.btn_seizo.setObjectName(u"btn_seizo")
        self.btn_seizo.setMinimumSize(QSize(0, 42))
        self.btn_seizo.setFont(font2)
        self.btn_seizo.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_seizo)

        self.spacer_sidebar = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_Sidebar.addItem(self.spacer_sidebar)


        self.horizontalLayout_Main.addWidget(self.Sidebar)

        self.stackedWidget = QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"/* \u2460 \u53f3\u5074\u30a8\u30ea\u30a2(QStackedWidget)\u306e\u4e2d\u306b\u3042\u308b\u5404\u30b7\u30b9\u30c6\u30e0\u30dc\u30bf\u30f3\u306e\u901a\u5e38\u30c7\u30b6\u30a4\u30f3\uff08\u767d\u6587\u5b57\u30cd\u30a4\u30d3\u30fc\uff09 */\n"
"QStackedWidget QPushButton#btn_JuchuShokai, \n"
"QStackedWidget QPushButton#btn_Urikake, \n"
"QStackedWidget QPushButton#btn_Nouhin {\n"
"    color: #ffffff;\n"
"    background-color: #1e3a8a;\n"
"    border: 1px solid #172554;\n"
"    border-radius: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u2461 \u30de\u30a6\u30b9\u3092\u4e57\u305b\u305f\u6642\uff08\u30db\u30d0\u30fc\uff09\u3001\u307e\u305f\u306fTab\u30ad\u30fc\u304c\u5f53\u305f\u3063\u3066\u3044\u308b\u6642\uff08\u30d5\u30a9\u30fc\u30ab\u30b9\uff09\u306e\u5b8c\u74a7\u306a\u30ab\u30e9\u30fc\u30c1\u30a7\u30f3\u30b8 */\n"
"QStackedWidget QPushButton#btn_JuchuShokai:hover, \n"
"QStackedWidget QPushButton#btn_Urikake:hover, \n"
"QStackedWidget QPushButton#btn_Nouhin:hover,\n"
"QStackedWidget QPushButton#btn_JuchuShokai:"
                        "focus, \n"
"QStackedWidget QPushButton#btn_Urikake:focus, \n"
"QStackedWidget QPushButton#btn_Nouhin:focus {\n"
"    background-color: #2563eb; /* \u9bae\u3084\u304b\u306a\u660e\u308b\u3044\u9752\u3078\u5909\u5316 */\n"
"    border-color: #60a5fa;     /* \u67a0\u7dda\u3092\u6c34\u8272\u3078\u5909\u5316 */\n"
"}\n"
"")
        self.page_common = QWidget()
        self.page_common.setObjectName(u"page_common")
        self.verticalLayout_common = QVBoxLayout(self.page_common)
        self.verticalLayout_common.setObjectName(u"verticalLayout_common")
        self.verticalLayout_common.setContentsMargins(30, 30, 30, 30)
        self.title_common = QLabel(self.page_common)
        self.title_common.setObjectName(u"title_common")
        font3 = QFont()
        font3.setFamilies([u"Meiryo"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.title_common.setFont(font3)
        self.title_common.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_common.addWidget(self.title_common)

        self.spacer_common_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_common.addItem(self.spacer_common_bottom)

        self.stackedWidget.addWidget(self.page_common)
        self.page_qa = QWidget()
        self.page_qa.setObjectName(u"page_qa")
        self.verticalLayout_qa = QVBoxLayout(self.page_qa)
        self.verticalLayout_qa.setObjectName(u"verticalLayout_qa")
        self.verticalLayout_qa.setContentsMargins(30, 30, 30, 30)
        self.title_qa = QLabel(self.page_qa)
        self.title_qa.setObjectName(u"title_qa")
        self.title_qa.setFont(font3)
        self.title_qa.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_qa.addWidget(self.title_qa)

        self.spacer_qa_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_qa.addItem(self.spacer_qa_bottom)

        self.stackedWidget.addWidget(self.page_qa)
        self.page_sales = QWidget()
        self.page_sales.setObjectName(u"page_sales")
        self.verticalLayout_sales = QVBoxLayout(self.page_sales)
        self.verticalLayout_sales.setObjectName(u"verticalLayout_sales")
        self.verticalLayout_sales.setContentsMargins(30, 30, 30, 30)
        self.title_sales = QLabel(self.page_sales)
        self.title_sales.setObjectName(u"title_sales")
        self.title_sales.setFont(font3)
        self.title_sales.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_sales.addWidget(self.title_sales)

        self.horizontalLayout_sales_btns = QHBoxLayout()
        self.horizontalLayout_sales_btns.setSpacing(20)
        self.horizontalLayout_sales_btns.setObjectName(u"horizontalLayout_sales_btns")
        self.btn_JuchuShokai = QPushButton(self.page_sales)
        self.btn_JuchuShokai.setObjectName(u"btn_JuchuShokai")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_JuchuShokai.sizePolicy().hasHeightForWidth())
        self.btn_JuchuShokai.setSizePolicy(sizePolicy)
        self.btn_JuchuShokai.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_sales_btns.addWidget(self.btn_JuchuShokai)

        self.spacer_sales_btns = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_sales_btns.addItem(self.spacer_sales_btns)


        self.verticalLayout_sales.addLayout(self.horizontalLayout_sales_btns)

        self.spacer_sales_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_sales.addItem(self.spacer_sales_bottom)

        self.stackedWidget.addWidget(self.page_sales)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.verticalLayout_admin = QVBoxLayout(self.page_admin)
        self.verticalLayout_admin.setObjectName(u"verticalLayout_admin")
        self.verticalLayout_admin.setContentsMargins(30, 30, 30, 30)
        self.title_admin = QLabel(self.page_admin)
        self.title_admin.setObjectName(u"title_admin")
        self.title_admin.setFont(font3)
        self.title_admin.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_admin.addWidget(self.title_admin)

        self.horizontalLayout_admin_btns = QHBoxLayout()
        self.horizontalLayout_admin_btns.setSpacing(20)
        self.horizontalLayout_admin_btns.setObjectName(u"horizontalLayout_admin_btns")
        self.btn_urikake = QPushButton(self.page_admin)
        self.btn_urikake.setObjectName(u"btn_urikake")
        self.btn_urikake.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_admin_btns.addWidget(self.btn_urikake)

        self.btn_Nouhin = QPushButton(self.page_admin)
        self.btn_Nouhin.setObjectName(u"btn_Nouhin")
        self.btn_Nouhin.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_admin_btns.addWidget(self.btn_Nouhin)

        self.spacer_admin_btns = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_admin_btns.addItem(self.spacer_admin_btns)


        self.verticalLayout_admin.addLayout(self.horizontalLayout_admin_btns)

        self.spacer_admin_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_admin.addItem(self.spacer_admin_bottom)

        self.stackedWidget.addWidget(self.page_admin)
        self.page_factory = QWidget()
        self.page_factory.setObjectName(u"page_factory")
        self.verticalLayout_factory = QVBoxLayout(self.page_factory)
        self.verticalLayout_factory.setObjectName(u"verticalLayout_factory")
        self.verticalLayout_factory.setContentsMargins(30, 30, 30, 30)
        self.title_factory = QLabel(self.page_factory)
        self.title_factory.setObjectName(u"title_factory")
        self.title_factory.setFont(font3)
        self.title_factory.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_factory.addWidget(self.title_factory)

        self.horizontalLayout_factory_btns = QHBoxLayout()
        self.horizontalLayout_factory_btns.setSpacing(20)
        self.horizontalLayout_factory_btns.setObjectName(u"horizontalLayout_factory_btns")
        self.spacer_factory_btns = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_factory_btns.addItem(self.spacer_factory_btns)


        self.verticalLayout_factory.addLayout(self.horizontalLayout_factory_btns)

        self.spacer_factory_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_factory.addItem(self.spacer_factory_bottom)

        self.stackedWidget.addWidget(self.page_factory)

        self.horizontalLayout_Main.addWidget(self.stackedWidget)

        MainMenuWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainMenuWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainMenuWindow)
    # setupUi

    def retranslateUi(self, MainMenuWindow):
        MainMenuWindow.setWindowTitle(QCoreApplication.translate("MainMenuWindow", u"\u696d\u52d9\u652f\u63f4\u30e1\u30cb\u30e5\u30fc", None))
        self.title_label.setText(QCoreApplication.translate("MainMenuWindow", u"\u696d\u52d9\u652f\u63f4\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_kyotsu.setText(QCoreApplication.translate("MainMenuWindow", u" \u5171\u901a", None))
        self.btn_hinshitsu.setText(QCoreApplication.translate("MainMenuWindow", u" \u54c1\u8cea\u4fdd\u8a3c\u90e8", None))
        self.btn_eigyo.setText(QCoreApplication.translate("MainMenuWindow", u" \u55b6\u696d\u6280\u8853\u90e8", None))
        self.btn_soumu.setText(QCoreApplication.translate("MainMenuWindow", u" \u7dcf\u52d9\u90e8", None))
        self.btn_seizo.setText(QCoreApplication.translate("MainMenuWindow", u" \u88fd\u9020\u90e8", None))
        self.title_common.setText(QCoreApplication.translate("MainMenuWindow", u"\u5171\u901a \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.title_qa.setText(QCoreApplication.translate("MainMenuWindow", u"\u54c1\u8cea\u4fdd\u8a3c\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.title_sales.setText(QCoreApplication.translate("MainMenuWindow", u"\u55b6\u696d\u6280\u8853\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_JuchuShokai.setText(QCoreApplication.translate("MainMenuWindow", u"\u53d7\u6ce8\u7167\u4f1a", None))
        self.title_admin.setText(QCoreApplication.translate("MainMenuWindow", u"\u7dcf\u52d9\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_urikake.setText(QCoreApplication.translate("MainMenuWindow", u"\u58f2\u639b\u91d1\u56de\u53ce\u72b6\u6cc1\u4e00\u89a7", None))
        self.btn_Nouhin.setText(QCoreApplication.translate("MainMenuWindow", u"\u7d0d\u54c1\u66f8\u306b\u57fa\u3065\u304f\u58f2\u4e0a\u5185\u8a33", None))
        self.title_factory.setText(QCoreApplication.translate("MainMenuWindow", u"\u88fd\u9020\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
    # retranslateUi

