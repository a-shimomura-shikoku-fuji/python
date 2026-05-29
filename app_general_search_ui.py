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
        MainWindow.resize(968, 671)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        MainWindow.setWindowIcon(icon)
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
"/* \u5165\u529b\u9805\u76ee\u30b3\u30f3\u30dc\u30dc\u30c3\u30af\u30b9\uff08QComboBox\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"\n"
"\n"
"/* \u8868\u793a\u9805\u76ee\u30e9\u30d9\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"label_disp_\"]  {\n"
"    background-color: #94a3b8;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u30d5\u30ec\u30fc\u30e0\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QFrame#frame_btn {\n"
""
                        "    background-color: #f1f5f9; \n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#frame_search_results {\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u30c6\u30fc\u30d6\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #475569;\n"
"    border: 1px solid #475569;\n"
"    padding: 1px;\n"
"    border-radius: 4px;\n"
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
"/* \u623b\u308b\u30dc"
                        "\u30bf\u30f3\u3001\u30af\u30ea\u30a2\u30dc\u30bf\u30f3\u306e\u30b9\u30bf\u30a4\u30eb */\n"
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
"}\n"
"\n"
"QComboBox, QTextEdit, QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4"
                        "px;\n"
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
        self.title_cond = QLabel(self.centralwidget)
        self.title_cond.setObjectName(u"title_cond")
        self.title_cond.setGeometry(QRect(30, 10, 81, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.title_cond.setFont(font1)
        self.label_target_table = QLabel(self.centralwidget)
        self.label_target_table.setObjectName(u"label_target_table")
        self.label_target_table.setGeometry(QRect(20, 40, 101, 21))
        self.label_target_table.setFont(font1)
        self.label_target_table.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cmb_table_name = QComboBox(self.centralwidget)
        self.cmb_table_name.setObjectName(u"cmb_table_name")
        self.cmb_table_name.setGeometry(QRect(120, 40, 161, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.cmb_table_name.setFont(font2)
        self.cmb_table_name.setEditable(True)
        self.label_condition_rules = QLabel(self.centralwidget)
        self.label_condition_rules.setObjectName(u"label_condition_rules")
        self.label_condition_rules.setGeometry(QRect(20, 70, 101, 21))
        self.label_condition_rules.setFont(font1)
        self.label_condition_rules.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cmb_column_name = QComboBox(self.centralwidget)
        self.cmb_column_name.setObjectName(u"cmb_column_name")
        self.cmb_column_name.setGeometry(QRect(120, 70, 160, 21))
        self.cmb_column_name.setFont(font2)
        self.cmb_operator = QComboBox(self.centralwidget)
        self.cmb_operator.setObjectName(u"cmb_operator")
        self.cmb_operator.setGeometry(QRect(290, 70, 110, 21))
        self.cmb_operator.setFont(font2)
        self.text_cond_value = QTextEdit(self.centralwidget)
        self.text_cond_value.setObjectName(u"text_cond_value")
        self.text_cond_value.setGeometry(QRect(410, 70, 191, 21))
        self.text_cond_value.setFont(font2)
        self.text_cond_value.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.btn_add_cond = QPushButton(self.centralwidget)
        self.btn_add_cond.setObjectName(u"btn_add_cond")
        self.btn_add_cond.setGeometry(QRect(710, 70, 50, 21))
        self.btn_add_cond.setStyleSheet(u"QPushButton { background-color: #2563eb; color: #ffffff !important; border-radius: 4px; font-weight: bold; } QPushButton:hover { background-color: #1d4ed8; }\n"
"")
        self.label_current_conditions = QLabel(self.centralwidget)
        self.label_current_conditions.setObjectName(u"label_current_conditions")
        self.label_current_conditions.setGeometry(QRect(20, 100, 101, 71))
        self.label_current_conditions.setFont(font1)
        self.label_current_conditions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.listWidget_conds = QListWidget(self.centralwidget)
        self.listWidget_conds.setObjectName(u"listWidget_conds")
        self.listWidget_conds.setGeometry(QRect(120, 100, 581, 71))
        self.listWidget_conds.setFont(font2)
        self.btn_del_cond = QPushButton(self.centralwidget)
        self.btn_del_cond.setObjectName(u"btn_del_cond")
        self.btn_del_cond.setGeometry(QRect(710, 100, 50, 21))
        self.btn_del_cond.setStyleSheet(u"QPushButton { background-color: #dc2626; color: #ffffff !important; border-radius: 4px; font-weight: bold; } QPushButton:hover { background-color: #b91c1c; }\n"
"")
        self.title_result = QLabel(self.centralwidget)
        self.title_result.setObjectName(u"title_result")
        self.title_result.setGeometry(QRect(30, 200, 81, 16))
        self.title_result.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 224, 931, 361))
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #475569;\n"
"    border: 1px solid #475569;\n"
"    padding: 1px;\n"
"    border-radius: 4px;\n"
"}\n"
"/* 1. \U00005217\U000030d8\U000030c3\U000030c0\U000030fc\U0000ff08\U00004e0a\U000090e8\U0000ff09\U0000306e\U000030c7\U000030b6\U000030a4\U000030f3\U00008a2d\U00005b9a */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: #94a3b8; /* \U000080cc\U0000666f\U00008272 */\n"
"    color: #ffffff;            /* \U00006587\U00005b57\U00008272 */\n"
"    font-weight: bold;         /* \U0000592a\U00005b57 */\n"
"    border: 1px solid #172554; /* \U000067a0\U00007dda */\n"
"    text-align: left;          /* \U00005de6\U00005bc4\U0000305b */\n"
"\U00003000/* \U0001f4a1\U00003010\U00003053\U00003053\U00003092\U00008ffd\U00008a18\U00003011\U00004e0a\U00004e0b\U0000306b12\U000030d4\U000030af\U000030bb\U000030eb\U0000306e\U00004f59\U0000767d\U00003092\U00004f5c\U0000308b\U00003053\U00003068\U00003067\U00003001\U000030d8\U000030c3\U000030c0"
                        "\U000030fc\U00003092\U00009ad8\U0000304f\U00003057\U0000307e\U00003059 */\n"
"    padding-top: 0px;\n"
"    padding-bottom: 0px;\n"
"}\n"
"\n"
"/* 2. \U0000884c\U000030d8\U000030c3\U000030c0\U000030fc\U0000ff08\U00005de6\U00005074\U0000ff09\U0000306e\U000030c7\U000030b6\U000030a4\U000030f3\U00008a2d\U00005b9a */\n"
"QHeaderView::section:vertical {\n"
"    background-color: #94a3b8; /* \U000080cc\U0000666f\U00008272 */\n"
"    color: #ffffff;            /* \U00006587\U00005b57\U00008272 */\n"
"    font-weight: bold;         /* \U0000592a\U00005b57 */\n"
"    border: 1px solid #172554; /* \U000067a0\U00007dda */\n"
"    \n"
"    /* \U0001f4a1\U00003010Qt6.11.1\U0000306e\U00007d76\U00005bfe\U000030eb\U000030fc\U000030eb\U00003011\n"
"       CSS\U0000306e text-align \U00003067\U0000306f\U0000306a\U0000304f\U00003001Qt\U00005185\U000090e8\U0000306e\U0000914d\U00007f6e\U000030d7\U000030ed\U000030d1\U000030c6\U000030a3\U00003092\U000076f4\U000063a5\U000053f3\U00005bc4\U0000305b(AlignRight)\U0000306b\U00004e0a\U000066f8"
                        "\U0000304d\U00003057\U0000307e\U00003059\U00003002\n"
"       \U00005927\U00006587\U00005b57\U000030fb\U00005c0f\U00006587\U00005b57\U00003092\U000053b3\U00005bc6\U0000306b\U0000533a\U00005225\U00003059\U0000308b\U0000305f\U00003081\U00003001\U00003053\U0000306e\U0000307e\U0000307e\U000030b3\U000030d4\U000030fc\U00003057\U00003066\U0000304f\U00003060\U00003055\U00003044\U00003002 */\n"
"    qproperty-defaultAlignment: 'AlignRight | AlignVCenter';\n"
"    \n"
"    padding-right: 6px;        /* \U00006570\U00005b57\U0000304c\U000067a0\U00007dda\U0000306b\U000030d9\U000030bf\U000030c3\U00003068\U0000304f\U00003063\U00003064\U0000304b\U0000306a\U00003044\U0000305f\U00003081\U0000306e\U00009699\U00009593 */\n"
"}\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setGeometry(QRect(20, 590, 931, 51))
        self.frame_btn.setStyleSheet(u"")
        self.btn_back = QPushButton(self.frame_btn)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 10, 51, 31))
        self.btn_back.setStyleSheet(u"QPushButton { background-color: #e2e8f0; color: #475569 !important; border: 1px solid #475569; border-radius: 6px; font-weight: bold; } QPushButton:hover { background-color: #cbd5e1; }")
        self.btn_exe_csv = QPushButton(self.frame_btn)
        self.btn_exe_csv.setObjectName(u"btn_exe_csv")
        self.btn_exe_csv.setGeometry(QRect(580, 10, 51, 31))
        self.btn_exe_csv.setStyleSheet(u"")
        self.btn_exe_inquiry = QPushButton(self.frame_btn)
        self.btn_exe_inquiry.setObjectName(u"btn_exe_inquiry")
        self.btn_exe_inquiry.setGeometry(QRect(460, 10, 51, 31))
        self.btn_exe_inquiry.setStyleSheet(u"")
        self.btn_clear = QPushButton(self.frame_btn)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(520, 10, 51, 31))
        self.btn_clear.setStyleSheet(u"")
        self.btn_dummy_1 = QPushButton(self.frame_btn)
        self.btn_dummy_1.setObjectName(u"btn_dummy_1")
        self.btn_dummy_1.setGeometry(QRect(100, 10, 51, 31))
        self.btn_dummy_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_1.setStyleSheet(u"")
        self.btn_dummy_2 = QPushButton(self.frame_btn)
        self.btn_dummy_2.setObjectName(u"btn_dummy_2")
        self.btn_dummy_2.setGeometry(QRect(160, 10, 51, 31))
        self.btn_dummy_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_2.setStyleSheet(u"")
        self.btn_dummy_3 = QPushButton(self.frame_btn)
        self.btn_dummy_3.setObjectName(u"btn_dummy_3")
        self.btn_dummy_3.setGeometry(QRect(220, 10, 51, 31))
        self.btn_dummy_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_3.setStyleSheet(u"")
        self.btn_dummy_4 = QPushButton(self.frame_btn)
        self.btn_dummy_4.setObjectName(u"btn_dummy_4")
        self.btn_dummy_4.setGeometry(QRect(280, 10, 51, 31))
        self.btn_dummy_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_4.setStyleSheet(u"")
        self.btn_dummy_5 = QPushButton(self.frame_btn)
        self.btn_dummy_5.setObjectName(u"btn_dummy_5")
        self.btn_dummy_5.setGeometry(QRect(340, 10, 51, 31))
        self.btn_dummy_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_5.setStyleSheet(u"")
        self.btn_dummy_6 = QPushButton(self.frame_btn)
        self.btn_dummy_6.setObjectName(u"btn_dummy_6")
        self.btn_dummy_6.setGeometry(QRect(400, 10, 51, 31))
        self.btn_dummy_6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_6.setStyleSheet(u"")
        self.cmb_join_type = QComboBox(self.centralwidget)
        self.cmb_join_type.setObjectName(u"cmb_join_type")
        self.cmb_join_type.setGeometry(QRect(610, 70, 89, 21))
        self.word_count = QLabel(self.centralwidget)
        self.word_count.setObjectName(u"word_count")
        self.word_count.setGeometry(QRect(110, 200, 71, 16))
        self.word_count.setFont(font1)
        self.word_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6c4e\u7528\u691c\u7d22", None))
        self.title_cond.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u6761\u4ef6\u8a2d\u5b9a\uff1e", None))
        self.label_target_table.setText(QCoreApplication.translate("MainWindow", u"\u5bfe\u8c61\u30c6\u30fc\u30d6\u30eb", None))
        self.label_condition_rules.setText(QCoreApplication.translate("MainWindow", u"\u6761\u4ef6\u306e\u898f\u5247", None))
        self.text_cond_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5024\u3092\u5165\u529b", None))
        self.btn_add_cond.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0", None))
        self.label_current_conditions.setText(QCoreApplication.translate("MainWindow", u"\u73fe\u5728\u306e\u6761\u4ef6", None))
        self.btn_del_cond.setText(QCoreApplication.translate("MainWindow", u"\u524a\u9664", None))
        self.title_result.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u7167\u4f1a\u7d50\u679c\uff1e", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_exe_csv.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.btn_exe_inquiry.setText(QCoreApplication.translate("MainWindow", u"\u7167\u4f1a", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.btn_dummy_1.setText("")
        self.btn_dummy_2.setText("")
        self.btn_dummy_3.setText("")
        self.btn_dummy_4.setText("")
        self.btn_dummy_5.setText("")
        self.btn_dummy_6.setText("")
        self.word_count.setText("")
    # retranslateUi

