# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textbrowserTestikWGHz.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(436, 269)
        Dialog.setStyleSheet(u"background-color: rgb(255, 216, 249);")
        self.textbrow_Test = QTextBrowser(Dialog)
        self.textbrow_Test.setObjectName(u"textbrow_Test")
        self.textbrow_Test.setGeometry(QRect(10, 20, 256, 192))
        self.textbrow_Test.setStyleSheet(u"font: 20pt \"\ub098\ub214\uba85\uc870\";\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 127);")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 50, 116, 134))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_Print = QPushButton(self.layoutWidget)
        self.btn_Print.setObjectName(u"btn_Print")
        self.btn_Print.setStyleSheet(u"QPushButton::hover\n"
"{\n"
"color: rgb(0, 0, 0);\n"
"background-color : lightgreen;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: rgb(255, 255, 0);\n"
"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_Print)

        self.btn_setText = QPushButton(self.layoutWidget)
        self.btn_setText.setObjectName(u"btn_setText")

        self.verticalLayout.addWidget(self.btn_setText)

        self.btn_appendText = QPushButton(self.layoutWidget)
        self.btn_appendText.setObjectName(u"btn_appendText")

        self.verticalLayout.addWidget(self.btn_appendText)

        self.btn_Clear = QPushButton(self.layoutWidget)
        self.btn_Clear.setObjectName(u"btn_Clear")

        self.verticalLayout.addWidget(self.btn_Clear)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_Print.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.btn_setText.setText(QCoreApplication.translate("Dialog", u"SetText", None))
        self.btn_appendText.setText(QCoreApplication.translate("Dialog", u"AppendText", None))
        self.btn_Clear.setText(QCoreApplication.translate("Dialog", u"Clear", None))
    # retranslateUi

