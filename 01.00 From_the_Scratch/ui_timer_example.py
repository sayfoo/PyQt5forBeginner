# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer_exampleZHWbyL.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(492, 339)
        font = QFont()
        font.setPointSize(20)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.disp_label = QLabel(Form)
        self.disp_label.setObjectName(u"disp_label")
        self.disp_label.setMinimumSize(QSize(301, 71))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.disp_label.setFont(font1)
        self.disp_label.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
"border-color: rgb(0, 255, 255);\n"
"border-width: 10px;")
        self.disp_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.disp_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.disp_clock = QLCDNumber(Form)
        self.disp_clock.setObjectName(u"disp_clock")
        self.disp_clock.setMinimumSize(QSize(250, 81))
        self.disp_clock.setLayoutDirection(Qt.LeftToRight)
        self.disp_clock.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.disp_clock.setDigitCount(8)
        self.disp_clock.setProperty("intValue", 12345678)

        self.horizontalLayout_3.addWidget(self.disp_clock)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.start_btn = QPushButton(Form)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMinimumSize(QSize(141, 41))
        font2 = QFont()
        font2.setPointSize(18)
        self.start_btn.setFont(font2)
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

        self.stop_btn = QPushButton(Form)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(141, 41))
        self.stop_btn.setFont(font2)
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


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.disp_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#aa0000;\">Current Date time here</span></p></body></html>", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
    # retranslateUi

