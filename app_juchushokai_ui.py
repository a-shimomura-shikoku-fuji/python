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
        MainWindow.resize(684, 612)
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
"    color: #ffffff;\n"
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
"QFrame#frame_search_results {\n"
""
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
"/* \u623b\u308b\u30dc\u30bf\u30f3\u3001\u30af\u30ea\u30a2\u30dc\u30bf\u30f3\u306e\u30b9\u30bf\u30a4\u30eb */\n"
"QPushButton#btn_back, \n"
"QPushButton#btn_cl"
                        "ear { \n"
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_btn = QFrame(self.centralwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setGeometry(QRect(20, 530, 641, 51))
        self.frame_btn.setStyleSheet(u"")
        self.frame_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_back = QPushButton(self.frame_btn)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 10, 51, 31))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_back.setFont(font1)
        self.btn_back.setStyleSheet(u"")
        self.btn_exe_prev = QPushButton(self.frame_btn)
        self.btn_exe_prev.setObjectName(u"btn_exe_prev")
        self.btn_exe_prev.setGeometry(QRect(100, 10, 51, 31))
        self.btn_exe_prev.setFont(font1)
        self.btn_exe_prev.setStyleSheet(u"")
        self.btn_exe_next = QPushButton(self.frame_btn)
        self.btn_exe_next.setObjectName(u"btn_exe_next")
        self.btn_exe_next.setGeometry(QRect(160, 10, 51, 31))
        self.btn_exe_next.setFont(font1)
        self.btn_exe_next.setStyleSheet(u"")
        self.btn_exe_inquiry = QPushButton(self.frame_btn)
        self.btn_exe_inquiry.setObjectName(u"btn_exe_inquiry")
        self.btn_exe_inquiry.setGeometry(QRect(460, 10, 51, 31))
        self.btn_exe_inquiry.setFont(font1)
        self.btn_exe_inquiry.setStyleSheet(u"")
        self.btn_clear = QPushButton(self.frame_btn)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(520, 10, 51, 31))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setBold(True)
        self.btn_clear.setFont(font2)
        self.btn_clear.setStyleSheet(u"")
        self.btn_dummy_1 = QPushButton(self.frame_btn)
        self.btn_dummy_1.setObjectName(u"btn_dummy_1")
        self.btn_dummy_1.setGeometry(QRect(220, 10, 51, 31))
        self.btn_dummy_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_1.setStyleSheet(u"")
        self.btn_dummy_2 = QPushButton(self.frame_btn)
        self.btn_dummy_2.setObjectName(u"btn_dummy_2")
        self.btn_dummy_2.setGeometry(QRect(280, 10, 51, 31))
        self.btn_dummy_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_2.setStyleSheet(u"")
        self.btn_dummy_3 = QPushButton(self.frame_btn)
        self.btn_dummy_3.setObjectName(u"btn_dummy_3")
        self.btn_dummy_3.setGeometry(QRect(340, 10, 51, 31))
        self.btn_dummy_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_3.setStyleSheet(u"")
        self.btn_dummy_4 = QPushButton(self.frame_btn)
        self.btn_dummy_4.setObjectName(u"btn_dummy_4")
        self.btn_dummy_4.setGeometry(QRect(400, 10, 51, 31))
        self.btn_dummy_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_4.setStyleSheet(u"")
        self.btn_dummy_5 = QPushButton(self.frame_btn)
        self.btn_dummy_5.setObjectName(u"btn_dummy_5")
        self.btn_dummy_5.setGeometry(QRect(580, 10, 51, 31))
        self.btn_dummy_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dummy_5.setStyleSheet(u"")
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
        self.tableWidget.setGeometry(QRect(20, 280, 641, 241))
        font3 = QFont()
        font3.setPointSize(10)
        self.tableWidget.setFont(font3)
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.data_tokname = QLabel(self.centralwidget)
        self.data_tokname.setObjectName(u"data_tokname")
        self.data_tokname.setGeometry(QRect(120, 180, 331, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.data_tokname.setFont(font4)
        self.label_disp_juchu_date = QLabel(self.centralwidget)
        self.label_disp_juchu_date.setObjectName(u"label_disp_juchu_date")
        self.label_disp_juchu_date.setGeometry(QRect(20, 160, 101, 21))
        self.label_disp_juchu_date.setFont(font4)
        self.label_disp_juchu_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_disp_tokname = QLabel(self.centralwidget)
        self.label_disp_tokname.setObjectName(u"label_disp_tokname")
        self.label_disp_tokname.setGeometry(QRect(20, 180, 101, 21))
        self.label_disp_tokname.setFont(font4)
        self.label_disp_tokname.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_disp_instructions = QLabel(self.centralwidget)
        self.label_disp_instructions.setObjectName(u"label_disp_instructions")
        self.label_disp_instructions.setGeometry(QRect(20, 200, 101, 71))
        self.label_disp_instructions.setFont(font4)
        self.label_disp_instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_disp_tanname = QLabel(self.centralwidget)
        self.label_disp_tanname.setObjectName(u"label_disp_tanname")
        self.label_disp_tanname.setGeometry(QRect(450, 180, 101, 21))
        self.label_disp_tanname.setFont(font4)
        self.label_disp_tanname.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_disp_nouki = QLabel(self.centralwidget)
        self.label_disp_nouki.setObjectName(u"label_disp_nouki")
        self.label_disp_nouki.setGeometry(QRect(450, 160, 101, 21))
        self.label_disp_nouki.setFont(font4)
        self.label_disp_nouki.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_nouki = QLabel(self.centralwidget)
        self.data_nouki.setObjectName(u"data_nouki")
        self.data_nouki.setGeometry(QRect(550, 160, 111, 21))
        self.data_nouki.setFont(font4)
        self.data_tok_chuban = QLabel(self.centralwidget)
        self.data_tok_chuban.setObjectName(u"data_tok_chuban")
        self.data_tok_chuban.setGeometry(QRect(330, 160, 121, 21))
        self.data_tok_chuban.setFont(font4)
        self.data_tanname = QLabel(self.centralwidget)
        self.data_tanname.setObjectName(u"data_tanname")
        self.data_tanname.setGeometry(QRect(550, 180, 111, 21))
        self.data_tanname.setFont(font4)
        self.data_juchu_date = QLabel(self.centralwidget)
        self.data_juchu_date.setObjectName(u"data_juchu_date")
        self.data_juchu_date.setGeometry(QRect(120, 160, 111, 21))
        self.data_juchu_date.setFont(font4)
        self.label_disp_tok_chuban = QLabel(self.centralwidget)
        self.label_disp_tok_chuban.setObjectName(u"label_disp_tok_chuban")
        self.label_disp_tok_chuban.setGeometry(QRect(230, 160, 101, 21))
        self.label_disp_tok_chuban.setFont(font4)
        self.label_disp_tok_chuban.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_nouki = QLabel(self.centralwidget)
        self.label_nouki.setObjectName(u"label_nouki")
        self.label_nouki.setGeometry(QRect(20, 40, 101, 21))
        self.label_nouki.setFont(font4)
        self.label_nouki.setStyleSheet(u"")
        self.label_nouki.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_inquiry_result = QLabel(self.centralwidget)
        self.title_inquiry_result.setObjectName(u"title_inquiry_result")
        self.title_inquiry_result.setGeometry(QRect(30, 130, 81, 16))
        self.title_inquiry_result.setFont(font4)
        self.title_inquiry_result.setStyleSheet(u"color: #1e3a8a;")
        self.word_nouki_from_to = QLabel(self.centralwidget)
        self.word_nouki_from_to.setObjectName(u"word_nouki_from_to")
        self.word_nouki_from_to.setGeometry(QRect(230, 40, 31, 21))
        self.word_nouki_from_to.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_juchu_date = QLabel(self.centralwidget)
        self.label_juchu_date.setObjectName(u"label_juchu_date")
        self.label_juchu_date.setGeometry(QRect(20, 70, 101, 21))
        self.label_juchu_date.setFont(font4)
        self.label_juchu_date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label_juchu_date_from_to = QLabel(self.centralwidget)
        self.word_label_juchu_date_from_to.setObjectName(u"word_label_juchu_date_from_to")
        self.word_label_juchu_date_from_to.setGeometry(QRect(230, 70, 31, 21))
        self.word_label_juchu_date_from_to.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tok_chuban = QLabel(self.centralwidget)
        self.label_tok_chuban.setObjectName(u"label_tok_chuban")
        self.label_tok_chuban.setGeometry(QRect(430, 40, 101, 21))
        self.label_tok_chuban.setFont(font4)
        self.label_tok_chuban.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tokname = QLabel(self.centralwidget)
        self.label_tokname.setObjectName(u"label_tokname")
        self.label_tokname.setGeometry(QRect(430, 70, 101, 21))
        self.label_tokname.setFont(font4)
        self.label_tokname.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_chuban = QTextEdit(self.centralwidget)
        self.text_chuban.setObjectName(u"text_chuban")
        self.text_chuban.setGeometry(QRect(530, 40, 131, 21))
        self.text_chuban.setFont(font3)
        self.text_chuban.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.date_nouki_from = QDateEdit(self.centralwidget)
        self.date_nouki_from.setObjectName(u"date_nouki_from")
        self.date_nouki_from.setGeometry(QRect(120, 40, 111, 21))
        self.date_nouki_from.setFont(font3)
        self.date_nouki_from.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_nouki_from.setCalendarPopup(True)
        self.date_nouki_to = QDateEdit(self.centralwidget)
        self.date_nouki_to.setObjectName(u"date_nouki_to")
        self.date_nouki_to.setGeometry(QRect(260, 40, 111, 21))
        self.date_nouki_to.setFont(font3)
        self.date_nouki_to.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_nouki_to.setCalendarPopup(True)
        self.date_juchu_date_from = QDateEdit(self.centralwidget)
        self.date_juchu_date_from.setObjectName(u"date_juchu_date_from")
        self.date_juchu_date_from.setGeometry(QRect(120, 70, 111, 21))
        self.date_juchu_date_from.setFont(font3)
        self.date_juchu_date_from.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_juchu_date_from.setCalendarPopup(True)
        self.date_juchu_date_to = QDateEdit(self.centralwidget)
        self.date_juchu_date_to.setObjectName(u"date_juchu_date_to")
        self.date_juchu_date_to.setGeometry(QRect(260, 70, 111, 21))
        self.date_juchu_date_to.setFont(font3)
        self.date_juchu_date_to.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.date_juchu_date_to.setCalendarPopup(True)
        self.word_count = QLabel(self.centralwidget)
        self.word_count.setObjectName(u"word_count")
        self.word_count.setGeometry(QRect(120, 130, 71, 16))
        self.word_count.setFont(font4)
        self.word_count.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.text_tanname = QTextEdit(self.centralwidget)
        self.text_tanname.setObjectName(u"text_tanname")
        self.text_tanname.setGeometry(QRect(530, 70, 131, 21))
        self.text_tanname.setFont(font3)
        self.text_tanname.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_instructions = QTextEdit(self.centralwidget)
        self.text_instructions.setObjectName(u"text_instructions")
        self.text_instructions.setGeometry(QRect(120, 200, 541, 71))
        self.text_instructions.setFont(font3)
        self.text_instructions.setStyleSheet(u"border: 1px solid #475569;")
        self.text_instructions.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chk_nouki = QCheckBox(self.centralwidget)
        self.chk_nouki.setObjectName(u"chk_nouki")
        self.chk_nouki.setGeometry(QRect(380, 40, 21, 21))
        self.chk_juchu_date = QCheckBox(self.centralwidget)
        self.chk_juchu_date.setObjectName(u"chk_juchu_date")
        self.chk_juchu_date.setGeometry(QRect(380, 70, 21, 21))
        self.title_search_results = QLabel(self.centralwidget)
        self.title_search_results.setObjectName(u"title_search_results")
        self.title_search_results.setGeometry(QRect(30, 10, 81, 16))
        self.title_search_results.setFont(font4)
        self.title_search_results.setStyleSheet(u"color: #1e3a8a;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_btn.raise_()
        self.tableWidget.raise_()
        self.data_tokname.raise_()
        self.label_disp_tokname.raise_()
        self.data_nouki.raise_()
        self.data_tok_chuban.raise_()
        self.data_tanname.raise_()
        self.data_juchu_date.raise_()
        self.label_disp_tok_chuban.raise_()
        self.label_nouki.raise_()
        self.title_inquiry_result.raise_()
        self.word_nouki_from_to.raise_()
        self.label_juchu_date.raise_()
        self.word_label_juchu_date_from_to.raise_()
        self.text_chuban.raise_()
        self.date_nouki_from.raise_()
        self.date_nouki_to.raise_()
        self.date_juchu_date_from.raise_()
        self.date_juchu_date_to.raise_()
        self.word_count.raise_()
        self.text_tanname.raise_()
        self.text_instructions.raise_()
        self.chk_nouki.raise_()
        self.chk_juchu_date.raise_()
        self.title_search_results.raise_()
        self.label_disp_juchu_date.raise_()
        self.label_disp_nouki.raise_()
        self.label_disp_tanname.raise_()
        self.label_disp_instructions.raise_()
        self.label_tok_chuban.raise_()
        self.label_tokname.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 684, 33))
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
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u623b\u308b", None))
        self.btn_exe_prev.setText(QCoreApplication.translate("MainWindow", u"\u524d\u3078", None))
        self.btn_exe_next.setText(QCoreApplication.translate("MainWindow", u"\u6b21\u3078", None))
        self.btn_exe_inquiry.setText(QCoreApplication.translate("MainWindow", u"\u7167\u4f1a", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30a2", None))
        self.btn_dummy_1.setText("")
        self.btn_dummy_2.setText("")
        self.btn_dummy_3.setText("")
        self.btn_dummy_4.setText("")
        self.btn_dummy_5.setText("")
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
        self.data_tokname.setText("")
        self.label_disp_juchu_date.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u65e5", None))
        self.label_disp_tokname.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148", None))
        self.label_disp_instructions.setText(QCoreApplication.translate("MainWindow", u"\u6307\u793a\u4e8b\u9805", None))
        self.label_disp_tanname.setText(QCoreApplication.translate("MainWindow", u"\u62c5\u5f53\u8005", None))
        self.label_disp_nouki.setText(QCoreApplication.translate("MainWindow", u"\u7d0d\u671f", None))
        self.data_nouki.setText("")
        self.data_tok_chuban.setText("")
        self.data_tanname.setText("")
        self.data_juchu_date.setText("")
        self.label_disp_tok_chuban.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u6ce8\u756a", None))
        self.label_nouki.setText(QCoreApplication.translate("MainWindow", u"\u7d0d\u671f", None))
        self.title_inquiry_result.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u7167\u4f1a\u7d50\u679c\uff1e", None))
        self.word_nouki_from_to.setText(QCoreApplication.translate("MainWindow", u"\uff5e", None))
        self.label_juchu_date.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8\u65e5", None))
        self.word_label_juchu_date_from_to.setText(QCoreApplication.translate("MainWindow", u"\uff5e", None))
        self.label_tok_chuban.setText(QCoreApplication.translate("MainWindow", u"\u5f97\u610f\u5148\u6ce8\u756a", None))
        self.label_tokname.setText(QCoreApplication.translate("MainWindow", u"\u62c5\u5f53\u8005", None))
        self.word_count.setText("")
        self.chk_nouki.setText("")
        self.chk_juchu_date.setText("")
        self.title_search_results.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u691c\u7d22\u6761\u4ef6\uff1e", None))
    # retranslateUi

