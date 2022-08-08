# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menulGrGqw.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 661)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/check-mark-8-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* ===================================================== */\n"
"/* set style for logo widget */\n"
"#logoWidget {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"#companyName {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ===================================================== */\n"
"/* set style for home button */\n"
"#pushButton {\n"
"	padding-left: 15px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"/* ===================================================== */\n"
"/* set style for all the menu buttons */\n"
"#menuWidget QPushButton {\n"
"	text-align: left;\n"
"	border: None;\n"
"}\n"
"\n"
"#menuWidget QPushButton:hover, #widget:hover, #widget_2:hover  {\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"#menuWidget QPushButton:disabled  {\n"
"	background-color: rgb(222, 222, 222);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* ===================================================== */\n"
"/* set style for logo second menu buttons */\n"
"#carsWidget QPushButton, #socialWidget QP"
                        "ushButton {\n"
"	padding-left: 40px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"/* ===================================================== */\n"
"/* set style for menu and content widget */\n"
"#stackedWidget, #menuWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: solid 1px rgb(0, 0, 0);\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionToolBar = QAction(MainWindow)
        self.actionToolBar.setObjectName(u"actionToolBar")
        self.actionToolBar.setCheckable(True)
        self.actionToolBar.setChecked(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/top-navigation-toolbar-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionToolBar.setIcon(icon1)
        self.actionMenu = QAction(MainWindow)
        self.actionMenu.setObjectName(u"actionMenu")
        self.actionMenu.setCheckable(True)
        self.actionMenu.setChecked(True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/menu-4-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMenu.setIcon(icon2)
        self.actionToyota = QAction(MainWindow)
        self.actionToyota.setObjectName(u"actionToyota")
        icon3 = QIcon()
        icon3.addFile(u":/icons/toyota-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionToyota.setIcon(icon3)
        self.actionLexus = QAction(MainWindow)
        self.actionLexus.setObjectName(u"actionLexus")
        icon4 = QIcon()
        icon4.addFile(u":/icons/lexus-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLexus.setIcon(icon4)
        self.actionMazda = QAction(MainWindow)
        self.actionMazda.setObjectName(u"actionMazda")
        icon5 = QIcon()
        icon5.addFile(u":/icons/mazda-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMazda.setIcon(icon5)
        self.actionYouTube = QAction(MainWindow)
        self.actionYouTube.setObjectName(u"actionYouTube")
        icon6 = QIcon()
        icon6.addFile(u":/icons/youtube-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionYouTube.setIcon(icon6)
        self.actionTumblr = QAction(MainWindow)
        self.actionTumblr.setObjectName(u"actionTumblr")
        icon7 = QIcon()
        icon7.addFile(u":/icons/tumblr-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTumblr.setIcon(icon7)
        self.actionCars = QAction(MainWindow)
        self.actionCars.setObjectName(u"actionCars")
        self.actionCars.setCheckable(True)
        self.actionCars.setChecked(True)
        icon8 = QIcon()
        icon8.addFile(u":/icons/car-25-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCars.setIcon(icon8)
        self.actionSocial_Media = QAction(MainWindow)
        self.actionSocial_Media.setObjectName(u"actionSocial_Media")
        self.actionSocial_Media.setCheckable(True)
        self.actionSocial_Media.setChecked(True)
        icon9 = QIcon()
        icon9.addFile(u":/icons/group-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSocial_Media.setIcon(icon9)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Exit.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(5)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(200, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 560))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.logoWidget = QWidget(self.scrollAreaWidgetContents)
        self.logoWidget.setObjectName(u"logoWidget")
        self.logoWidget.setMinimumSize(QSize(0, 58))
        self.logoWidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.logoWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.logoImg = QLabel(self.logoWidget)
        self.logoImg.setObjectName(u"logoImg")
        self.logoImg.setMinimumSize(QSize(40, 40))
        self.logoImg.setMaximumSize(QSize(40, 40))
        self.logoImg.setPixmap(QPixmap(u":/icons/twitch-tv-2-48.ico"))
        self.logoImg.setScaledContents(True)
        self.logoImg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logoImg)

        self.companyName = QLabel(self.logoWidget)
        self.companyName.setObjectName(u"companyName")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        self.companyName.setFont(font1)

        self.horizontalLayout.addWidget(self.companyName)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.logoWidget, 0, 0, 1, 1)

        self.menuWidget = QWidget(self.scrollAreaWidgetContents)
        self.menuWidget.setObjectName(u"menuWidget")
        self.verticalLayout_3 = QVBoxLayout(self.menuWidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeWidget = QWidget(self.menuWidget)
        self.homeWidget.setObjectName(u"homeWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.homeWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.homeWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon10 = QIcon()
        icon10.addFile(u":/icons/home-4-48.ico", QSize(), QIcon.Disabled, QIcon.On)
        self.pushButton.setIcon(icon10)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.homeWidget)

        self.widget = QWidget(self.menuWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 5, 15, 5)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(16, 16))
        self.label_2.setMaximumSize(QSize(16, 16))
        self.label_2.setPixmap(QPixmap(u":/icons/car-25-48.ico"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)
        icon11 = QIcon()
        icon11.addFile(u":/icons/arrow-29-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/arrow-208-32.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.carsWidget = QWidget(self.menuWidget)
        self.carsWidget.setObjectName(u"carsWidget")
        self.verticalLayout = QVBoxLayout(self.carsWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.carsWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.carsWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_8 = QPushButton(self.carsWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_8)


        self.verticalLayout_3.addWidget(self.carsWidget)

        self.widget_2 = QWidget(self.menuWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 5, 15, 5)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(16, 16))
        self.label_3.setMaximumSize(QSize(16, 16))
        self.label_3.setPixmap(QPixmap(u":/icons/group-48.ico"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.socialWidget = QWidget(self.menuWidget)
        self.socialWidget.setObjectName(u"socialWidget")
        self.verticalLayout_2 = QVBoxLayout(self.socialWidget)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.socialWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.socialWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.verticalLayout_3.addWidget(self.socialWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.menuWidget, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)
        self.contentWidget = QWidget(self.splitter)
        self.contentWidget.setObjectName(u"contentWidget")
        self.verticalLayout_4 = QVBoxLayout(self.contentWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoWidget_2 = QWidget(self.contentWidget)
        self.logoWidget_2.setObjectName(u"logoWidget_2")
        self.logoWidget_2.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_5 = QHBoxLayout(self.logoWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.logoImg_2 = QLabel(self.logoWidget_2)
        self.logoImg_2.setObjectName(u"logoImg_2")
        self.logoImg_2.setMinimumSize(QSize(30, 30))
        self.logoImg_2.setMaximumSize(QSize(30, 30))
        self.logoImg_2.setPixmap(QPixmap(u":/icons/home-4-48.ico"))
        self.logoImg_2.setScaledContents(True)
        self.logoImg_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.logoImg_2)

        self.companyName_2 = QLabel(self.logoWidget_2)
        self.companyName_2.setObjectName(u"companyName_2")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        self.companyName_2.setFont(font2)

        self.horizontalLayout_5.addWidget(self.companyName_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addWidget(self.logoWidget_2)

        self.scrollArea_2 = QScrollArea(self.contentWidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 769, 500))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font3 = QFont()
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.stackedWidget.setFont(font3)
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.stackedWidget.setAutoFillBackground(False)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        font4 = QFont()
        font4.setPointSize(9)
        self.page.setFont(font4)
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(15)
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setPointSize(16)
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_7 = QGridLayout(self.page_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_8 = QGridLayout(self.page_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_9 = QGridLayout(self.page_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.splitter.addWidget(self.contentWidget)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 980, 22))
        self.menuFile_F = QMenu(self.menubar)
        self.menuFile_F.setObjectName(u"menuFile_F")
        self.menuView_V = QMenu(self.menubar)
        self.menuView_V.setObjectName(u"menuView_V")
        self.menuCars = QMenu(self.menubar)
        self.menuCars.setObjectName(u"menuCars")
        self.menuSocial_Media_S = QMenu(self.menubar)
        self.menuSocial_Media_S.setObjectName(u"menuSocial_Media_S")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        self.toolBar_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QToolBar(MainWindow)
        self.toolBar_3.setObjectName(u"toolBar_3")
        self.toolBar_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_3)

        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuView_V.menuAction())
        self.menubar.addAction(self.menuCars.menuAction())
        self.menubar.addAction(self.menuSocial_Media_S.menuAction())
        self.menuFile_F.addAction(self.action_Exit)
        self.menuView_V.addAction(self.actionToolBar)
        self.menuView_V.addAction(self.actionMenu)
        self.menuView_V.addAction(self.actionCars)
        self.menuView_V.addAction(self.actionSocial_Media)
        self.menuCars.addAction(self.actionToyota)
        self.menuCars.addAction(self.actionLexus)
        self.menuCars.addAction(self.actionMazda)
        self.menuSocial_Media_S.addAction(self.actionYouTube)
        self.menuSocial_Media_S.addAction(self.actionTumblr)
        self.toolBar.addAction(self.actionToolBar)
        self.toolBar.addAction(self.actionMenu)
        self.toolBar.addAction(self.actionCars)
        self.toolBar.addAction(self.actionSocial_Media)
        self.toolBar_2.addAction(self.actionToyota)
        self.toolBar_2.addAction(self.actionLexus)
        self.toolBar_2.addAction(self.actionMazda)
        self.toolBar_3.addAction(self.actionYouTube)
        self.toolBar_3.addAction(self.actionTumblr)

        self.retranslateUi(MainWindow)
        self.actionToolBar.toggled.connect(self.toolBar_3.setVisible)
        self.pushButton_5.toggled.connect(self.socialWidget.setVisible)
        self.actionToolBar.toggled.connect(self.toolBar.setVisible)
        self.actionToolBar.toggled.connect(self.toolBar_2.setVisible)
        self.pushButton_2.toggled.connect(self.carsWidget.setVisible)
        self.actionCars.toggled.connect(self.toolBar_2.setVisible)
        self.actionSocial_Media.toggled.connect(self.toolBar_3.setVisible)
        self.actionMenu.toggled.connect(self.scrollArea.setVisible)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionToolBar.setText(QCoreApplication.translate("MainWindow", u"ToolBar", None))
        self.actionMenu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.actionToyota.setText(QCoreApplication.translate("MainWindow", u"Toyota", None))
        self.actionLexus.setText(QCoreApplication.translate("MainWindow", u"Lexus", None))
        self.actionMazda.setText(QCoreApplication.translate("MainWindow", u"Mazda", None))
        self.actionYouTube.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.actionTumblr.setText(QCoreApplication.translate("MainWindow", u"Tumblr", None))
        self.actionCars.setText(QCoreApplication.translate("MainWindow", u"Cars", None))
        self.actionSocial_Media.setText(QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.actionSocial_Media.setIconText(QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.logoImg.setText("")
        self.companyName.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cars", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Toyota", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Lexus", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Mazda", None))
        self.label_3.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Tumblr", None))
        self.logoImg_2.setText("")
        self.companyName_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Toyata", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lexus", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mazda", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tumblr", None))
        self.menuFile_F.setTitle(QCoreApplication.translate("MainWindow", u"File(&F)", None))
        self.menuView_V.setTitle(QCoreApplication.translate("MainWindow", u"View(&V)", None))
        self.menuCars.setTitle(QCoreApplication.translate("MainWindow", u"Cars(&C)", None))
        self.menuSocial_Media_S.setTitle(QCoreApplication.translate("MainWindow", u"Social Media(&S)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.toolBar_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_3", None))
    # retranslateUi

