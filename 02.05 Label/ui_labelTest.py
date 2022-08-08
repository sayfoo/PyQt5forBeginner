# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'labelTestnZrfEg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.lbl_Test = QLabel(Dialog)
        self.lbl_Test.setObjectName(u"lbl_Test")
        self.lbl_Test.setGeometry(QRect(50, 70, 291, 61))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.lbl_Test.setFont(font)
        self.lbl_Test.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 0, 0);\n"
"font: 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_changeText = QPushButton(Dialog)
        self.btn_changeText.setObjectName(u"btn_changeText")
        self.btn_changeText.setGeometry(QRect(92, 160, 116, 32))
        self.btn_printText = QPushButton(Dialog)
        self.btn_printText.setObjectName(u"btn_printText")
        self.btn_printText.setGeometry(QRect(210, 160, 98, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_Test.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">This is Label - Display Text</span></p></body></html>", None))
        self.btn_changeText.setText(QCoreApplication.translate("Dialog", u"ChangeText", None))
        self.btn_printText.setText(QCoreApplication.translate("Dialog", u"PrintText", None))
    # retranslateUi

