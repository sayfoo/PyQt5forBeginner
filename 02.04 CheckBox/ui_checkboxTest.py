# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkboxTestNijQzd.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.chk_3 = QCheckBox(Dialog)
        self.chk_3.setObjectName(u"chk_3")
        self.chk_3.setGeometry(QRect(50, 142, 95, 20))
        self.chk_3.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.chk_2 = QCheckBox(Dialog)
        self.chk_2.setObjectName(u"chk_2")
        self.chk_2.setGeometry(QRect(50, 121, 95, 20))
        self.chk_2.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.chk_4 = QCheckBox(Dialog)
        self.chk_4.setObjectName(u"chk_4")
        self.chk_4.setGeometry(QRect(50, 163, 95, 20))
        self.chk_4.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.chk_1 = QCheckBox(Dialog)
        self.chk_1.setObjectName(u"chk_1")
        self.chk_1.setGeometry(QRect(50, 100, 95, 20))
        self.chk_1.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(190, 80, 171, 121))
        self.groupBox.setStyleSheet(u"background-color: rgb(140, 184, 255);")
        self.groupchk_3 = QCheckBox(self.groupBox)
        self.groupchk_3.setObjectName(u"groupchk_3")
        self.groupchk_3.setGeometry(QRect(10, 71, 120, 20))
        self.groupchk_1 = QCheckBox(self.groupBox)
        self.groupchk_1.setObjectName(u"groupchk_1")
        self.groupchk_1.setGeometry(QRect(10, 29, 120, 20))
        self.groupchk_4 = QCheckBox(self.groupBox)
        self.groupchk_4.setObjectName(u"groupchk_4")
        self.groupchk_4.setGeometry(QRect(10, 92, 120, 20))
        self.groupchk_2 = QCheckBox(self.groupBox)
        self.groupchk_2.setObjectName(u"groupchk_2")
        self.groupchk_2.setGeometry(QRect(10, 50, 120, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.chk_3.setText(QCoreApplication.translate("Dialog", u"CheckBox3", None))
        self.chk_2.setText(QCoreApplication.translate("Dialog", u"CheckBox2", None))
        self.chk_4.setText(QCoreApplication.translate("Dialog", u"CheckBox4", None))
        self.chk_1.setText(QCoreApplication.translate("Dialog", u"CheckBox1", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"GroupBox", None))
        self.groupchk_3.setText(QCoreApplication.translate("Dialog", u"GroupCheck3", None))
        self.groupchk_1.setText(QCoreApplication.translate("Dialog", u"GroupCheck1", None))
        self.groupchk_4.setText(QCoreApplication.translate("Dialog", u"GroupCheck4", None))
        self.groupchk_2.setText(QCoreApplication.translate("Dialog", u"GroupCheck2", None))
    # retranslateUi

