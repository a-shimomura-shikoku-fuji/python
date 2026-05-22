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
"/* \u5de6\u5074\u30ca\u30d3\u30b2\u30fc\u30b7\u30e7\u30f3\u30dc\u30bf\u30f3 */\n"
"QFrame#Sidebar QPushButton {\n"
"    color: #cbd5e1 !important; \n"
"    background-color: transparent !important; \n"
"    text-align: left;\n"
"    padding-left: 15px; \n"
"    border: none !important; \n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#Sidebar QPushButton:hover { color: #ffffff !important; background-color: #1e293b !important; }\n"
"QFrame#Sidebar QPushButton:checked { color: #ffffff !important; background-color: #2563eb !important; font-weight: bold; }\n"
"\n"
"/* \u53f3\u5074\u696d\u52d9\u6a5f\u80fd\u30dc\u30bf\u30f3\uff08\u55b6\u696d\u6280\u8853\u90e8\u30fb\u7dcf\u52d9\u90e8\u5171\u901a\u306e\u6d17\u7df4\u3055\u308c\u305f\u30cd\u30a4\u30d3\u30fc\u30c7\u30b6\u30a4\u30f3\uff09 */\n"
"QStackedWidget QPushButton {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff !important;\n"
"    border-radius: 6px;\n"
" "
                        "   font-size: 11pt;\n"
"    font-weight: bold;\n"
"    border: 1px solid #172554;\n"
"}\n"
"QStackedWidget QPushButton:hover, QStackedWidget QPushButton:focus {\n"
"    background-color: #2563eb;\n"
"    color: #ffffff !important;\n"
"    border: 1px solid #60a5fa;\n"
"}\n"
"QStackedWidget QPushButton:disabled {\n"
"    background-color: #f1f5f9;\n"
"    color: #94a3b8 !important;\n"
"    border: 1px solid #e2e8f0;\n"
"}")
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
        self.verticalLayout_Sidebar = QVBoxLayout(self.Sidebar)
        self.verticalLayout_Sidebar.setSpacing(8)
        self.verticalLayout_Sidebar.setObjectName(u"verticalLayout_Sidebar")
        self.verticalLayout_Sidebar.setContentsMargins(10, 20, 10, 20)
        self.title_label = QLabel(self.Sidebar)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamilies([u"Meiryo"])
        font.setPointSize(13)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: #ffffff; margin-bottom: 15px;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_Sidebar.addWidget(self.title_label)

        self.btn_common = QPushButton(self.Sidebar)
        self.btn_common.setObjectName(u"btn_common")
        self.btn_common.setMinimumSize(QSize(0, 42))
        font1 = QFont()
        font1.setFamilies([u"Meiryo"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_common.setFont(font1)
        self.btn_common.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_common)

        self.btn_qa = QPushButton(self.Sidebar)
        self.btn_qa.setObjectName(u"btn_qa")
        self.btn_qa.setMinimumSize(QSize(0, 42))
        self.btn_qa.setFont(font1)
        self.btn_qa.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_qa)

        self.btn_sales = QPushButton(self.Sidebar)
        self.btn_sales.setObjectName(u"btn_sales")
        self.btn_sales.setMinimumSize(QSize(0, 42))
        self.btn_sales.setFont(font1)
        self.btn_sales.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_sales)

        self.btn_admin = QPushButton(self.Sidebar)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setMinimumSize(QSize(0, 42))
        self.btn_admin.setFont(font1)
        self.btn_admin.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_admin)

        self.btn_factory = QPushButton(self.Sidebar)
        self.btn_factory.setObjectName(u"btn_factory")
        self.btn_factory.setMinimumSize(QSize(0, 42))
        self.btn_factory.setFont(font1)
        self.btn_factory.setCheckable(True)

        self.verticalLayout_Sidebar.addWidget(self.btn_factory)

        self.spacer_sidebar = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_Sidebar.addItem(self.spacer_sidebar)


        self.horizontalLayout_Main.addWidget(self.Sidebar)

        self.stackedWidget = QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #f8fafc;")
        self.page_common = QWidget()
        self.page_common.setObjectName(u"page_common")
        self.verticalLayout_common = QVBoxLayout(self.page_common)
        self.verticalLayout_common.setObjectName(u"verticalLayout_common")
        self.verticalLayout_common.setContentsMargins(30, 30, 30, 30)
        self.title_common = QLabel(self.page_common)
        self.title_common.setObjectName(u"title_common")
        font2 = QFont()
        font2.setFamilies([u"Meiryo"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.title_common.setFont(font2)
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
        self.title_qa.setFont(font2)
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
        self.title_sales.setFont(font2)
        self.title_sales.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_sales.addWidget(self.title_sales)

        self.horizontalLayout_sales_btns = QHBoxLayout()
        self.horizontalLayout_sales_btns.setSpacing(20)
        self.horizontalLayout_sales_btns.setObjectName(u"horizontalLayout_sales_btns")
        self.btn_juchu = QPushButton(self.page_sales)
        self.btn_juchu.setObjectName(u"btn_juchu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_juchu.sizePolicy().hasHeightForWidth())
        self.btn_juchu.setSizePolicy(sizePolicy)
        self.btn_juchu.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_sales_btns.addWidget(self.btn_juchu)

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
        self.title_admin.setFont(font2)
        self.title_admin.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_admin.addWidget(self.title_admin)

        self.horizontalLayout_admin_btns = QHBoxLayout()
        self.horizontalLayout_admin_btns.setSpacing(20)
        self.horizontalLayout_admin_btns.setObjectName(u"horizontalLayout_admin_btns")
        self.btn_urikake = QPushButton(self.page_admin)
        self.btn_urikake.setObjectName(u"btn_urikake")
        self.btn_urikake.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_admin_btns.addWidget(self.btn_urikake)

        self.btn_uriage_utivake = QPushButton(self.page_admin)
        self.btn_uriage_utivake.setObjectName(u"btn_uriage_utivake")
        self.btn_uriage_utivake.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_admin_btns.addWidget(self.btn_uriage_utivake)

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
        self.title_factory.setFont(font2)
        self.title_factory.setStyleSheet(u"color: #1e293b; margin-bottom: 20px;")

        self.verticalLayout_factory.addWidget(self.title_factory)

        self.horizontalLayout_factory_btns = QHBoxLayout()
        self.horizontalLayout_factory_btns.setSpacing(20)
        self.horizontalLayout_factory_btns.setObjectName(u"horizontalLayout_factory_btns")
        self.btn_seizu = QPushButton(self.page_factory)
        self.btn_seizu.setObjectName(u"btn_seizu")
        self.btn_seizu.setEnabled(False)
        self.btn_seizu.setMinimumSize(QSize(160, 80))

        self.horizontalLayout_factory_btns.addWidget(self.btn_seizu)

        self.spacer_factory_btns = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_factory_btns.addItem(self.spacer_factory_btns)


        self.verticalLayout_factory.addLayout(self.horizontalLayout_factory_btns)

        self.spacer_factory_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_factory.addItem(self.spacer_factory_bottom)

        self.stackedWidget.addWidget(self.page_factory)

        self.horizontalLayout_Main.addWidget(self.stackedWidget)

        MainMenuWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainMenuWindow)

        QMetaObject.connectSlotsByName(MainMenuWindow)
    # setupUi

    def retranslateUi(self, MainMenuWindow):
        MainMenuWindow.setWindowTitle(QCoreApplication.translate("MainMenuWindow", u"\u696d\u52d9\u652f\u63f4\u30e1\u30cb\u30e5\u30fc", None))
        self.title_label.setText(QCoreApplication.translate("MainMenuWindow", u"\u696d\u52d9\u652f\u63f4\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_common.setText(QCoreApplication.translate("MainMenuWindow", u" \u5171\u901a", None))
        self.btn_qa.setText(QCoreApplication.translate("MainMenuWindow", u" \u54c1\u8cea\u4fdd\u8a3c\u90e8", None))
        self.btn_sales.setText(QCoreApplication.translate("MainMenuWindow", u" \u55b6\u696d\u6280\u8853\u90e8", None))
        self.btn_admin.setText(QCoreApplication.translate("MainMenuWindow", u" \u7dcf\u52d9\u90e8", None))
        self.btn_factory.setText(QCoreApplication.translate("MainMenuWindow", u" \u88fd\u9020\u90e8", None))
        self.title_common.setText(QCoreApplication.translate("MainMenuWindow", u"\u5171\u901a \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.title_qa.setText(QCoreApplication.translate("MainMenuWindow", u"\u54c1\u8cea\u4fdd\u8a3c\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.title_sales.setText(QCoreApplication.translate("MainMenuWindow", u"\u55b6\u696d\u6280\u8853\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_juchu.setText(QCoreApplication.translate("MainMenuWindow", u"\u53d7\u6ce8\u7167\u4f1a", None))
        self.title_admin.setText(QCoreApplication.translate("MainMenuWindow", u"\u7dcf\u52d9\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_urikake.setText(QCoreApplication.translate("MainMenuWindow", u"\u58f2\u639b\u91d1\u56de\u53ce\u72b6\u6cc1\u4e00\u89a7", None))
        self.btn_uriage_utivake.setText(QCoreApplication.translate("MainMenuWindow", u"\u58f2\u4e0a\u5185\u8a33\u4e00\u89a7", None))
        self.title_factory.setText(QCoreApplication.translate("MainMenuWindow", u"\u88fd\u9020\u90e8 \u696d\u52d9\u30e1\u30cb\u30e5\u30fc", None))
        self.btn_seizu.setText(QCoreApplication.translate("MainMenuWindow", u"\u751f\u7523\u8a08\u753b\u767b\u9332(\u958b\u767a\u4e2d)", None))
    # retranslateUi

