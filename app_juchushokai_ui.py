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
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 628)
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
"/* \u30e9\u30d9\u30eb\uff1a\u8868\u793a\u9805\u76ee\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"label_disp_\"]  {\n"
"    background-color: #94a3b8;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #64748b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u30e9\u30d9\u30eb\uff1a\u8868\u793a\u30c7\u30fc\u30bf\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QLabel[objectName^=\"data_\"]  {\n"
"    background-c"
                        "olor: #f1f5f9;\n"
"    color: #334155;\n"
"    font-weight: bold;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"/* \u5165\u529b\u9805\u76ee\uff1a\u30c6\u30ad\u30b9\u30c8\uff08QTextEdit\uff09\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QTextEdit {\n"
"    background-color: #ffffff;\n"
"    color: #0f172a;\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"}\n"
"QTextEdit:focus {\n"
"    background-color: #f8fafc;\n"
"    border: 1px solid #3b82f6;\n"
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
"/* \u30c6\u30fc\u30d6\u30eb\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QTableWidget {\n"
"    backgroun"
                        "d-color: #ffffff;\n"
"    gridline-color: #64748b;\n"
"    border: 1px solid #94a3b8;\n"
"    padding: 1px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u30dc\u30bf\u30f3\uff1a\u901a\u5e38\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton[objectName^=\"btn_exe_\"] {\n"
"    background-color: #1e3a8a;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #64748b;\n"
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
"QPushButto"
                        "n#btn_back:hover, \n"
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
"/* \u30dc\u30bf\u30f3\uff1a\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton[objectName^=\"btn_dummy_\"] {\n"
"    background-color: #f1f5f9; \n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/*\u30d5\u30ec\u30fc\u30e0\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QFrame#frame_btn {\n"
"    background-color: #cbd5e1; \n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#frame_search_results {\n"
"    border: 1px solid #94a3b8;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 10)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(640, 75))
        self.widget.setMaximumSize(QSize(640, 75))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.date_juchu_date_to = QDateEdit(self.widget)
        self.date_juchu_date_to.setObjectName(u"date_juchu_date_to")
        self.date_juchu_date_to.setMinimumSize(QSize(111, 21))
        self.date_juchu_date_to.setMaximumSize(QSize(111, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.date_juchu_date_to.setFont(font1)
        self.date_juchu_date_to.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_juchu_date_to.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_juchu_date_to, 2, 3, 1, 1)

        self.chk_juchu_date = QCheckBox(self.widget)
        self.chk_juchu_date.setObjectName(u"chk_juchu_date")
        self.chk_juchu_date.setMinimumSize(QSize(21, 21))
        self.chk_juchu_date.setMaximumSize(QSize(21, 21))

        self.gridLayout.addWidget(self.chk_juchu_date, 2, 4, 1, 1)

        self.label_tok_chuban = QLabel(self.widget)
        self.label_tok_chuban.setObjectName(u"label_tok_chuban")
        self.label_tok_chuban.setMinimumSize(QSize(101, 21))
        self.label_tok_chuban.setMaximumSize(QSize(101, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_tok_chuban.setFont(font2)
        self.label_tok_chuban.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_tok_chuban, 1, 6, 1, 1)

        self.text_chuban = QTextEdit(self.widget)
        self.text_chuban.setObjectName(u"text_chuban")
        self.text_chuban.setMinimumSize(QSize(131, 21))
        self.text_chuban.setMaximumSize(QSize(131, 21))
        self.text_chuban.setFont(font1)
        self.text_chuban.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.text_chuban, 1, 7, 1, 1)

        self.label_tokname = QLabel(self.widget)
        self.label_tokname.setObjectName(u"label_tokname")
        self.label_tokname.setMinimumSize(QSize(101, 21))
        self.label_tokname.setMaximumSize(QSize(101, 21))
        self.label_tokname.setFont(font2)
        self.label_tokname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_tokname, 2, 6, 1, 1)

        self.label_nouki = QLabel(self.widget)
        self.label_nouki.setObjectName(u"label_nouki")
        self.label_nouki.setMinimumSize(QSize(101, 21))
        self.label_nouki.setMaximumSize(QSize(101, 21))
        self.label_nouki.setFont(font2)
        self.label_nouki.setStyleSheet(u"")
        self.label_nouki.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_nouki, 1, 0, 1, 1)

        self.title_search_results = QLabel(self.widget)
        self.title_search_results.setObjectName(u"title_search_results")
        self.title_search_results.setMinimumSize(QSize(101, 21))
        self.title_search_results.setMaximumSize(QSize(101, 21))
        self.title_search_results.setFont(font2)
        self.title_search_results.setStyleSheet(u"color: #1e3a8a;")

        self.gridLayout.addWidget(self.title_search_results, 0, 0, 1, 2)

        self.date_nouki_to = QDateEdit(self.widget)
        self.date_nouki_to.setObjectName(u"date_nouki_to")
        self.date_nouki_to.setMinimumSize(QSize(111, 21))
        self.date_nouki_to.setMaximumSize(QSize(111, 21))
        self.date_nouki_to.setFont(font1)
        self.date_nouki_to.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_nouki_to.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_nouki_to, 1, 3, 1, 1)

        self.date_nouki_from = QDateEdit(self.widget)
        self.date_nouki_from.setObjectName(u"date_nouki_from")
        self.date_nouki_from.setMinimumSize(QSize(111, 21))
        self.date_nouki_from.setMaximumSize(QSize(111, 21))
        self.date_nouki_from.setFont(font1)
        self.date_nouki_from.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_nouki_from.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_nouki_from, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 5, 2, 1)

        self.text_tanname = QTextEdit(self.widget)
        self.text_tanname.setObjectName(u"text_tanname")
        self.text_tanname.setMinimumSize(QSize(131, 21))
        self.text_tanname.setMaximumSize(QSize(131, 21))
        self.text_tanname.setFont(font1)
        self.text_tanname.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.text_tanname, 2, 7, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 8, 1, 1)

        self.word_label_juchu_date_from_to = QLabel(self.widget)
        self.word_label_juchu_date_from_to.setObjectName(u"word_label_juchu_date_from_to")
        self.word_label_juchu_date_from_to.setMinimumSize(QSize(21, 21))
        self.word_label_juchu_date_from_to.setMaximumSize(QSize(21, 21))
        self.word_label_juchu_date_from_to.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.word_label_juchu_date_from_to, 2, 2, 1, 1)

        self.chk_nouki = QCheckBox(self.widget)
        self.chk_nouki.setObjectName(u"chk_nouki")
        self.chk_nouki.setMinimumSize(QSize(21, 21))
        self.chk_nouki.setMaximumSize(QSize(21, 21))

        self.gridLayout.addWidget(self.chk_nouki, 1, 4, 1, 1)

        self.date_juchu_date_from = QDateEdit(self.widget)
        self.date_juchu_date_from.setObjectName(u"date_juchu_date_from")
        self.date_juchu_date_from.setMinimumSize(QSize(111, 21))
        self.date_juchu_date_from.setMaximumSize(QSize(111, 21))
        self.date_juchu_date_from.setFont(font1)
        self.date_juchu_date_from.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_juchu_date_from.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_juchu_date_from, 2, 1, 1, 1)

        self.label_juchu_date = QLabel(self.widget)
        self.label_juchu_date.setObjectName(u"label_juchu_date")
        self.label_juchu_date.setMinimumSize(QSize(101, 21))
        self.label_juchu_date.setMaximumSize(QSize(101, 21))
        self.label_juchu_date.setFont(font2)
        self.label_juchu_date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_juchu_date, 2, 0, 1, 1)

        self.word_nouki_from_to = QLabel(self.widget)
        self.word_nouki_from_to.setObjectName(u"word_nouki_from_to")
        self.word_nouki_from_to.setMinimumSize(QSize(21, 21))
        self.word_nouki_from_to.setMaximumSize(QSize(21, 21))
        self.word_nouki_from_to.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.word_nouki_from_to, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(660, 400))
        self.widget_2.setMaximumSize(QSize(660, 400))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_2)
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
        self.tableWidget.setMinimumSize(QSize(652, 245))
        self.tableWidget.setMaximumSize(QSize(652, 245))
        self.tableWidget.setFont(font1)
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.horizontalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableWidget, 5, 0, 1, 6)

        self.label_disp_juchu_date = QLabel(self.widget_2)
        self.label_disp_juchu_date.setObjectName(u"label_disp_juchu_date")
        self.label_disp_juchu_date.setMinimumSize(QSize(101, 21))
        self.label_disp_juchu_date.setMaximumSize(QSize(101, 21))
        self.label_disp_juchu_date.setFont(font2)
        self.label_disp_juchu_date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_disp_juchu_date, 2, 0, 1, 1)

        self.label_disp_tok_chuban = QLabel(self.widget_2)
        self.label_disp_tok_chuban.setObjectName(u"label_disp_tok_chuban")
        self.label_disp_tok_chuban.setMinimumSize(QSize(101, 21))
        self.label_disp_tok_chuban.setMaximumSize(QSize(101, 21))
        self.label_disp_tok_chuban.setFont(font2)
        self.label_disp_tok_chuban.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_disp_tok_chuban, 2, 2, 1, 1)

        self.data_tok_chuban = QLabel(self.widget_2)
        self.data_tok_chuban.setObjectName(u"data_tok_chuban")
        self.data_tok_chuban.setMinimumSize(QSize(121, 21))
        self.data_tok_chuban.setMaximumSize(QSize(121, 21))
        self.data_tok_chuban.setFont(font2)

        self.gridLayout_2.addWidget(self.data_tok_chuban, 2, 3, 1, 1)

        self.data_juchu_date = QLabel(self.widget_2)
        self.data_juchu_date.setObjectName(u"data_juchu_date")
        self.data_juchu_date.setMinimumSize(QSize(111, 21))
        self.data_juchu_date.setMaximumSize(QSize(111, 21))
        self.data_juchu_date.setFont(font2)

        self.gridLayout_2.addWidget(self.data_juchu_date, 2, 1, 1, 1)

        self.data_tokname = QLabel(self.widget_2)
        self.data_tokname.setObjectName(u"data_tokname")
        self.data_tokname.setMinimumSize(QSize(336, 21))
        self.data_tokname.setMaximumSize(QSize(336, 21))
        self.data_tokname.setFont(font2)

        self.gridLayout_2.addWidget(self.data_tokname, 3, 1, 1, 3)

        self.data_nouki = QLabel(self.widget_2)
        self.data_nouki.setObjectName(u"data_nouki")
        self.data_nouki.setMinimumSize(QSize(111, 21))
        self.data_nouki.setMaximumSize(QSize(111, 21))
        self.data_nouki.setFont(font2)

        self.gridLayout_2.addWidget(self.data_nouki, 2, 5, 1, 1)

        self.label_disp_tokname = QLabel(self.widget_2)
        self.label_disp_tokname.setObjectName(u"label_disp_tokname")
        self.label_disp_tokname.setMinimumSize(QSize(101, 21))
        self.label_disp_tokname.setMaximumSize(QSize(101, 21))
        self.label_disp_tokname.setFont(font2)
        self.label_disp_tokname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_disp_tokname, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 6, 1, 1)

        self.label_disp_instructions = QLabel(self.widget_2)
        self.label_disp_instructions.setObjectName(u"label_disp_instructions")
        self.label_disp_instructions.setMinimumSize(QSize(101, 71))
        self.label_disp_instructions.setMaximumSize(QSize(101, 71))
        self.label_disp_instructions.setFont(font2)
        self.label_disp_instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_disp_instructions, 4, 0, 1, 1)

        self.word_count = QLabel(self.widget_2)
        self.word_count.setObjectName(u"word_count")
        self.word_count.setMinimumSize(QSize(71, 21))
        self.word_count.setMaximumSize(QSize(71, 21))
        self.word_count.setFont(font2)
        self.word_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.word_count, 0, 1, 1, 1)

        self.data_tanname = QLabel(self.widget_2)
        self.data_tanname.setObjectName(u"data_tanname")
        self.data_tanname.setMinimumSize(QSize(111, 21))
        self.data_tanname.setMaximumSize(QSize(111, 21))
        self.data_tanname.setFont(font2)

        self.gridLayout_2.addWidget(self.data_tanname, 3, 5, 1, 1)

        self.text_instructions = QTextEdit(self.widget_2)
        self.text_instructions.setObjectName(u"text_instructions")
        self.text_instructions.setMinimumSize(QSize(549, 71))
        self.text_instructions.setMaximumSize(QSize(550, 71))
        self.text_instructions.setFont(font1)
        self.text_instructions.setStyleSheet(u"")
        self.text_instructions.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.text_instructions, 4, 1, 1, 5)

        self.label_disp_tanname = QLabel(self.widget_2)
        self.label_disp_tanname.setObjectName(u"label_disp_tanname")
        self.label_disp_tanname.setMinimumSize(QSize(101, 21))
        self.label_disp_tanname.setMaximumSize(QSize(101, 21))
        self.label_disp_tanname.setFont(font2)
        self.label_disp_tanname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_disp_tanname, 3, 4, 1, 1)

        self.title_inquiry_result = QLabel(self.widget_2)
        self.title_inquiry_result.setObjectName(u"title_inquiry_result")
        self.title_inquiry_result.setMinimumSize(QSize(101, 21))
        self.title_inquiry_result.setMaximumSize(QSize(101, 21))
        self.title_inquiry_result.setFont(font2)
        self.title_inquiry_result.setStyleSheet(u"color: #1e3a8a;")

        self.gridLayout_2.addWidget(self.title_inquiry_result, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.label_disp_nouki = QLabel(self.widget_2)
        self.label_disp_nouki.setObjectName(u"label_disp_nouki")
        self.label_disp_nouki.setMinimumSize(QSize(101, 21))
        self.label_disp_nouki.setMaximumSize(QSize(101, 21))
        self.label_disp_nouki.setFont(font2)
        self.label_disp_nouki.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_disp_nouki, 2, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(622, 51))
        self.frame_btn.setMaximumSize(QSize(622, 51))
        self.frame_btn.setStyleSheet(u"")
        self.frame_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btn)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 9, -1)
        self.btn_back = QPushButton(self.frame_btn)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(51, 31))
        self.btn_back.setMaximumSize(QSize(51, 31))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_back.setFont(font3)
        self.btn_back.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_exe_prev = QPushButton(self.frame_btn)
        self.btn_exe_prev.setObjectName(u"btn_exe_prev")
        self.btn_exe_prev.setMinimumSize(QSize(51, 31))
        self.btn_exe_prev.setMaximumSize(QSize(51, 31))
        self.btn_exe_prev.setFont(font3)
        self.btn_exe_prev.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_exe_prev)

        self.btn_exe_next = QPushButton(self.frame_btn)
        self.btn_exe_next.setObjectName(u"btn_exe_next")
        self.btn_exe_next.setMinimumSize(QSize(51, 31))
        self.btn_exe_next.setMaximumSize(QSize(51, 31))
        self.btn_exe_next.setFont(font3)
        self.btn_exe_next.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_exe_next)

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

        self.btn_dummy_4 = QPushButton(self.frame_btn)
        self.btn_dummy_4.setObjectName(u"btn_dummy_4")
        self.btn_dummy_4.setMinimumSize(QSize(51, 31))
        self.btn_dummy_4.setMaximumSize(QSize(51, 31))
        self.btn_dummy_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_4.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_dummy_4)

        self.btn_exe_inquiry = QPushButton(self.frame_btn)
        self.btn_exe_inquiry.setObjectName(u"btn_exe_inquiry")
        self.btn_exe_inquiry.setMinimumSize(QSize(51, 31))
        self.btn_exe_inquiry.setMaximumSize(QSize(51, 31))
        self.btn_exe_inquiry.setFont(font3)
        self.btn_exe_inquiry.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_exe_inquiry)

        self.btn_clear = QPushButton(self.frame_btn)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(51, 31))
        self.btn_clear.setMaximumSize(QSize(51, 31))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI"])
        font4.setBold(True)
        self.btn_clear.setFont(font4)
        self.btn_clear.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_clear)

        self.btn_dummy_5 = QPushButton(self.frame_btn)
        self.btn_dummy_5.setObjectName(u"btn_dummy_5")
        self.btn_dummy_5.setMinimumSize(QSize(51, 31))
        self.btn_dummy_5.setMaximumSize(QSize(51, 31))
        self.btn_dummy_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_5.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_dummy_5)


        self.verticalLayout.addWidget(self.frame_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.date_nouki_from, self.date_nouki_to)
        QWidget.setTabOrder(self.date_nouki_to, self.chk_nouki)
        QWidget.setTabOrder(self.chk_nouki, self.date_juchu_date_from)
        QWidget.setTabOrder(self.date_juchu_date_from, self.date_juchu_date_to)
        QWidget.setTabOrder(self.date_juchu_date_to, self.chk_juchu_date)
        QWidget.setTabOrder(self.chk_juchu_date, self.text_chuban)
        QWidget.setTabOrder(self.text_chuban, self.text_tanname)
        QWidget.setTabOrder(self.text_tanname, self.text_instructions)
        QWidget.setTabOrder(self.text_instructions, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.btn_back)
        QWidget.setTabOrder(self.btn_back, self.btn_exe_prev)
        QWidget.setTabOrder(self.btn_exe_prev, self.btn_exe_next)
        QWidget.setTabOrder(self.btn_exe_next, self.btn_exe_inquiry)
        QWidget.setTabOrder(self.btn_exe_inquiry, self.btn_clear)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u7167\u4f1a", None))
        self.chk_juchu_date.setText("")
        self.label_tok_chuban.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u6ce8\u756a", None))
        self.label_tokname.setText(QCoreApplication.translate("MainWindow", u"\u62c5\u5f53\u8005", None))
        self.label_nouki.setText(QCoreApplication.translate("MainWindow", u"\u7d0d\u671f", None))
        self.title_search_results.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u6761\u4ef6\uff1e", None))
        self.word_label_juchu_date_from_to.setText(QCoreApplication.translate("MainWindow", u"\uff5e", None))
        self.chk_nouki.setText("")
        self.label_juchu_date.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u65e5", None))
        self.word_nouki_from_to.setText(QCoreApplication.translate("MainWindow", u"\uff5e", None))
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
        self.label_disp_juchu_date.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u65e5", None))
        self.label_disp_tok_chuban.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u6ce8\u756a", None))
        self.data_tok_chuban.setText("")
        self.data_juchu_date.setText("")
        self.data_tokname.setText("")
        self.data_nouki.setText("")
        self.label_disp_tokname.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148", None))
        self.label_disp_instructions.setText(QCoreApplication.translate("MainWindow", u"\u6307\u793a\u4e8b\u9805", None))
        self.word_count.setText("")
        self.data_tanname.setText("")
        self.label_disp_tanname.setText(QCoreApplication.translate("MainWindow", u"\u62c5\u5f53\u8005", None))
        self.title_inquiry_result.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u7167\u4f1a\u7d50\u679c\uff1e", None))
        self.label_disp_nouki.setText(QCoreApplication.translate("MainWindow", u"\u7d0d\u671f", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_exe_prev.setText(QCoreApplication.translate("MainWindow", u"\u524d\u3078", None))
        self.btn_exe_next.setText(QCoreApplication.translate("MainWindow", u"\u6b21\u3078", None))
        self.btn_dummy_1.setText("")
        self.btn_dummy_2.setText("")
        self.btn_dummy_3.setText("")
        self.btn_dummy_4.setText("")
        self.btn_exe_inquiry.setText(QCoreApplication.translate("MainWindow", u"\u7167\u4f1a", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.btn_dummy_5.setText("")
    # retranslateUi

