# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainDialogTWFduC.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 340)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 211, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.labelUSD = QLabel(Dialog)
        self.labelUSD.setObjectName(u"labelUSD")
        self.labelUSD.setGeometry(QRect(95, 189, 24, 16))
        self.labelKRW = QLabel(Dialog)
        self.labelKRW.setObjectName(u"labelKRW")
        self.labelKRW.setGeometry(QRect(95, 218, 31, 16))
        self.labelJPY = QLabel(Dialog)
        self.labelJPY.setObjectName(u"labelJPY")
        self.labelJPY.setGeometry(QRect(95, 247, 20, 16))
        self.lineEditUSD = QLineEdit(Dialog)
        self.lineEditUSD.setObjectName(u"lineEditUSD")
        self.lineEditUSD.setGeometry(QRect(160, 189, 137, 22))
        self.lineEditKRW = QLineEdit(Dialog)
        self.lineEditKRW.setObjectName(u"lineEditKRW")
        self.lineEditKRW.setGeometry(QRect(160, 218, 137, 22))
        self.lineEditJPY = QLineEdit(Dialog)
        self.lineEditJPY.setObjectName(u"lineEditJPY")
        self.lineEditJPY.setGeometry(QRect(160, 247, 137, 22))
        self.labelLogo = QLabel(Dialog)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(260, 20, 101, 101))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(95, 160, 58, 16))
        self.comboBoxReferenceCurrency = QComboBox(Dialog)
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.setObjectName(u"comboBoxReferenceCurrency")
        self.comboBoxReferenceCurrency.setGeometry(QRect(160, 160, 73, 22))
        self.pushButtonConfigure = QPushButton(Dialog)
        self.pushButtonConfigure.setObjectName(u"pushButtonConfigure")
        self.pushButtonConfigure.setGeometry(QRect(90, 290, 93, 28))
        self.pushButtonLoadRates = QPushButton(Dialog)
        self.pushButtonLoadRates.setObjectName(u"pushButtonLoadRates")
        self.pushButtonLoadRates.setGeometry(QRect(190, 290, 93, 28))
        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(300, 290, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Currency Converter", None))
        self.labelUSD.setText(QCoreApplication.translate("Dialog", u"USD", None))
        self.labelKRW.setText(QCoreApplication.translate("Dialog", u"KRW", None))
        self.labelJPY.setText(QCoreApplication.translate("Dialog", u"JPY", None))
        self.labelLogo.setText(QCoreApplication.translate("Dialog", u"Logo", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Reference", None))
        self.comboBoxReferenceCurrency.setItemText(0, QCoreApplication.translate("Dialog", u"USD", None))
        self.comboBoxReferenceCurrency.setItemText(1, QCoreApplication.translate("Dialog", u"KRW", None))
        self.comboBoxReferenceCurrency.setItemText(2, QCoreApplication.translate("Dialog", u"JPY", None))

        self.pushButtonConfigure.setText(QCoreApplication.translate("Dialog", u"Configure", None))
        self.pushButtonLoadRates.setText(QCoreApplication.translate("Dialog", u"Load Rates", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"confirm", None))
    # retranslateUi

