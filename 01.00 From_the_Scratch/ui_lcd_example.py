# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lcd_exampleskKMTD.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(554, 258)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(0)
        self.frame_01 = QFrame(self.splitter)
        self.frame_01.setObjectName(u"frame_01")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_01.sizePolicy().hasHeightForWidth())
        self.frame_01.setSizePolicy(sizePolicy)
        self.frame_01.setMinimumSize(QSize(0, 100))
        self.frame_01.setFrameShape(QFrame.StyledPanel)
        self.frame_01.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_01)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.disp_label = QLabel(self.frame_01)
        self.disp_label.setObjectName(u"disp_label")
        self.disp_label.setMinimumSize(QSize(301, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.disp_label.setFont(font)
        self.disp_label.setStyleSheet(u"QLabel {\n"
"background-color: rgb(255, 170, 127);\n"
"border-style: outset;\n"
"border-color: rgb(255,0, 255);\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"padding: 3px; \n"
"}")
        self.disp_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.disp_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_2.setStretch(1, 2)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.frame_01)
        self.frame_02 = QFrame(self.splitter)
        self.frame_02.setObjectName(u"frame_02")
        self.frame_02.setMinimumSize(QSize(0, 70))
        self.frame_02.setFrameShape(QFrame.Panel)
        self.frame_02.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_02)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.disp_clock = QLCDNumber(self.frame_02)
        self.disp_clock.setObjectName(u"disp_clock")
        self.disp_clock.setMinimumSize(QSize(250, 70))
        self.disp_clock.setLayoutDirection(Qt.LeftToRight)
        self.disp_clock.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.disp_clock.setDigitCount(8)
        self.disp_clock.setProperty("intValue", 12345678)

        self.horizontalLayout_3.addWidget(self.disp_clock)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.frame_02)
        self.frame_03 = QFrame(self.splitter)
        self.frame_03.setObjectName(u"frame_03")
        self.frame_03.setMinimumSize(QSize(0, 70))
        self.frame_03.setFrameShape(QFrame.StyledPanel)
        self.frame_03.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_03)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.start_btn = QPushButton(self.frame_03)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMinimumSize(QSize(141, 65))
        font1 = QFont()
        font1.setPointSize(18)
        self.start_btn.setFont(font1)
        self.start_btn.setStyleSheet(u"QPushButton::hover\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"background-color : lightgreen;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 0, 0);\n"
"padding: 2px;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: rgb(0, 255, 255);\n"
"background-color: rgb(255, 0, 255);\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 0, 0);\n"
"padding: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.start_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stop_btn = QPushButton(self.frame_03)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(141, 65))
        self.stop_btn.setFont(font1)
        self.stop_btn.setStyleSheet(u"QPushButton::hover\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"background-color : lightgreen;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 0, 0);\n"
"padding: 2px;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: rgb(0, 255, 255);\n"
"background-color: rgb(255, 0, 255);\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 0, 0);\n"
"padding: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.stop_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.frame_03)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.disp_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#aa0000;\">Current Date time here</span></p></body></html>", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
    # retranslateUi

