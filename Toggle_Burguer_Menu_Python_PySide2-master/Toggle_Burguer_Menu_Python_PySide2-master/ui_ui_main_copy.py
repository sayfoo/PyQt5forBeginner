# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_copyKnaDsX.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
# import main_rcc_rc
import main_rcc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 567)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"######!background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 70))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(255, 0, 255);")
        self.Top_Bar.setFrameShape(QFrame.StyledPanel)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(100, 70))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_toggle)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        self.Btn_Toggle.setMinimumSize(QSize(0, 50))
        self.Btn_Toggle.setMaximumSize(QSize(16777215, 16777215))
        self.Btn_Toggle.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame = QFrame(self.Top_Bar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setStyleSheet(u"background-color: rgb(170, 170, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        self.title_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.title_label)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.Top_Bar)

        self.Contents = QFrame(self.centralwidget)
        self.Contents.setObjectName(u"Contents")
        self.Contents.setStyleSheet(u"background-color: rgb(255, 0, 255);")
        self.Contents.setFrameShape(QFrame.StyledPanel)
        self.Contents.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Contents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Contents)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 50))
        self.btn_page_1.setStyleSheet(u"background-color: rgb(170, 255, 0);")

        self.verticalLayout_3.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 50))
        self.btn_page_2.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.verticalLayout_3.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 50))
        self.btn_page_3.setStyleSheet(u"background-color: rgb(133, 170, 85);")

        self.verticalLayout_3.addWidget(self.btn_page_3)

        self.verticalSpacer = QSpacerItem(20, 356, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_top_menus)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.stackedWidget = QStackedWidget(self.Contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font1 = QFont()
        font1.setPointSize(40)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: #FFF;")
        self.label_1.setPixmap(QPixmap(u":/images/images/fig_01.png"))
        self.label_1.setScaledContents(True)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(36)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setPixmap(QPixmap(u":/images/images/fig_02.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font3.setPointSize(36)
        font3.setBold(False)
        font3.setItalic(False)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setPixmap(QPixmap(u":/images/images/fig_03.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.Contents)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"James Web", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.label_1.setText("")
        self.label_2.setText("")
        self.label.setText("")
    # retranslateUi

