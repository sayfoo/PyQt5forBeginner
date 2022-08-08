# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lineeditTestxIubdD.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 171)
        self.lbl_textHere = QLabel(Dialog)
        self.lbl_textHere.setObjectName(u"lbl_textHere")
        self.lbl_textHere.setGeometry(QRect(30, 50, 351, 16))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 351, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineedit_Test = QLineEdit(self.layoutWidget)
        self.lineedit_Test.setObjectName(u"lineedit_Test")

        self.horizontalLayout.addWidget(self.lineedit_Test)

        self.btn_changeText = QPushButton(self.layoutWidget)
        self.btn_changeText.setObjectName(u"btn_changeText")

        self.horizontalLayout.addWidget(self.btn_changeText)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_textHere.setText(QCoreApplication.translate("Dialog", u"Text Here", None))
        self.btn_changeText.setText(QCoreApplication.translate("Dialog", u"Change Label Text", None))
    # retranslateUi

