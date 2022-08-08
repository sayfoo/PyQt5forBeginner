# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_excel_fileqXLbPj.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(916, 773)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(Form)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background-color: rgb(210, 255, 233);")

        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.file_name = QLabel(Form)
        self.file_name.setObjectName(u"file_name")

        self.horizontalLayout_3.addWidget(self.file_name)

        self.show_name = QLineEdit(Form)
        self.show_name.setObjectName(u"show_name")
        self.show_name.setEnabled(False)
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.show_name.setFont(font)
        self.show_name.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: rgb(85, 255, 255);")

        self.horizontalLayout_3.addWidget(self.show_name)

        self.open_btn = QPushButton(Form)
        self.open_btn.setObjectName(u"open_btn")
        font1 = QFont()
        font1.setPointSize(12)
        self.open_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.open_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(4, 1)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.load_btn = QPushButton(Form)
        self.load_btn.setObjectName(u"load_btn")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.load_btn.setFont(font2)
        self.load_btn.setStyleSheet(u"QPushButton::hover\n"
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

        self.horizontalLayout.addWidget(self.load_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.file_name.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">File Name</span></p></body></html>", None))
        self.show_name.setPlaceholderText(QCoreApplication.translate("Form", u"excel file name", None))
        self.open_btn.setText(QCoreApplication.translate("Form", u"Open Button", None))
        self.load_btn.setText(QCoreApplication.translate("Form", u"Load Excel File", None))
    # retranslateUi

