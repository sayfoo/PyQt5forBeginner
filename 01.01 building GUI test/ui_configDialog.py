# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configDialogTpFihC.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 165)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 171, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 171, 41))
        self.pushButtonSave = QPushButton(Dialog)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(100, 120, 93, 28))
        self.pushButtonClose = QPushButton(Dialog)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setGeometry(QRect(210, 120, 93, 28))
        self.comboBoxDefaultReferenceCurrency = QComboBox(Dialog)
        self.comboBoxDefaultReferenceCurrency.addItem("")
        self.comboBoxDefaultReferenceCurrency.addItem("")
        self.comboBoxDefaultReferenceCurrency.addItem("")
        self.comboBoxDefaultReferenceCurrency.setObjectName(u"comboBoxDefaultReferenceCurrency")
        self.comboBoxDefaultReferenceCurrency.setGeometry(QRect(200, 70, 73, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Configure Settings", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Default Reference Currency", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.pushButtonClose.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.comboBoxDefaultReferenceCurrency.setItemText(0, QCoreApplication.translate("Dialog", u"USD", None))
        self.comboBoxDefaultReferenceCurrency.setItemText(1, QCoreApplication.translate("Dialog", u"KRW", None))
        self.comboBoxDefaultReferenceCurrency.setItemText(2, QCoreApplication.translate("Dialog", u"JPY", None))

    # retranslateUi

