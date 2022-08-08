# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radiobuttonTestjFOZCG.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(438, 343)
        Dialog.setStyleSheet(u"background-color: rgb(129, 255, 158);")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(150, 90, 161, 171))
        self.groupBox.setStyleSheet(u"background-color: rgb(232, 117, 255);")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_rad1 = QRadioButton(self.groupBox)
        self.groupBox_rad1.setObjectName(u"groupBox_rad1")

        self.verticalLayout.addWidget(self.groupBox_rad1)

        self.groupBox_rad2 = QRadioButton(self.groupBox)
        self.groupBox_rad2.setObjectName(u"groupBox_rad2")

        self.verticalLayout.addWidget(self.groupBox_rad2)

        self.groupBox_rad3 = QRadioButton(self.groupBox)
        self.groupBox_rad3.setObjectName(u"groupBox_rad3")

        self.verticalLayout.addWidget(self.groupBox_rad3)

        self.groupBox_rad4 = QRadioButton(self.groupBox)
        self.groupBox_rad4.setObjectName(u"groupBox_rad4")

        self.verticalLayout.addWidget(self.groupBox_rad4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"GroupBox", None))
        self.groupBox_rad1.setText(QCoreApplication.translate("Dialog", u"groupBox1", None))
        self.groupBox_rad2.setText(QCoreApplication.translate("Dialog", u"groupBox2", None))
        self.groupBox_rad3.setText(QCoreApplication.translate("Dialog", u"groupBox3", None))
        self.groupBox_rad4.setText(QCoreApplication.translate("Dialog", u"groupBox4", None))
    # retranslateUi

