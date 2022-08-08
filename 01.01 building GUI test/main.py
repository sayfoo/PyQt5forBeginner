import sys
from functools import partial
from PySide6.QtWidgets import (QApplication, QMainWindow,
                              QWidget, QPushButton, QHBoxLayout, QVBoxLayout)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtTest import QTest
from PySide6.QtGui import QFont, QColor, QPixmap
from ui_mainDialog import Ui_Dialog as Main
from ui_configDialog import Ui_Dialog as Config

import requests
import pickle
import os, time

global CONFIG_FILE
circular = 0
CONFIG_FILE = 'config.pkl'


class ConfigParameters(QWidget, Config):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        with open(CONFIG_FILE, 'rb') as f:
            self.config = pickle.load(f)

        self.comboBoxDefaultReferenceCurrency.setCurrentText(self.config['ref_currency'])

        self.pushButtonSave.clicked.connect(self.update_config)
        self.pushButtonClose.clicked.connect(self.close_window)

    def update_config(self):

        self.config['ref_currency'] = self.comboBoxDefaultReferenceCurrency.currentText()

        with open(CONFIG_FILE, 'wb') as f:
            pickle.dump(self.config, f)

    def close_window(self):
        self.close()


class MainDialog(QWidget, Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'rb') as f:
                self.config = pickle.load(f)
        else:
            with open(CONFIG_FILE, 'wb') as f:
                self.config = {'ref_currency': 'USD'}
                pickle.dump(self.config, f)

        pixmap = QPixmap('logo.png')
        self.labelLogo.setPixmap(pixmap)
        self.labelLogo.setScaledContents(True)

        self.comboBoxReferenceCurrency.setCurrentText(self.config['ref_currency'])

        self.pushButtonLoadRates.clicked.connect(self.load_rates)
        self.pushButtonConfigure.clicked.connect(self.open_config_window)
        self.confirm.clicked.connect(self.confirmed)

    def confirmed(self):
        global circular
        match circular % 4:
            case 0:
                self.lineEditUSD.setText("아아 미국 시험중..")
            case 1:
                self.lineEditKRW.setText("아아 한국 시험중..")
            case 2:
                self.lineEditJPY.setText("아아 일본 시험중..")
            case 3:
                self.lineEditJPY.clear()
                QTest.qWait(1000)
                self.lineEditKRW.clear()
                QTest.qWait(1000)
                self.lineEditUSD.clear()
        circular += 1

    def open_config_window(self):
        self.configParameters = ConfigParameters()
        self.configParameters.show()

        with open(CONFIG_FILE, 'rb') as f:
            self.config = pickle.load(f)

        self.comboBoxReferenceCurrency.setCurrentText(self.config['ref_currency'])

    def load_rates(self):
        print("잠시만 기둘려...")
        self.lineEditUSD.setText("아아 잠시만..")

        reference = self.comboBoxReferenceCurrency.currentText()

        print(f"{reference = }")
        url = 'https://api.exchangerate-api.com/v4/latest/' + reference
        response = requests.get(url)
        data = response.json()
        QTest.qWait(1000)
        self.lineEditUSD.setText(str(data['rates']['USD']))
        self.lineEditKRW.setText(str(data['rates']['KRW']))
        self.lineEditJPY.setText(str(data['rates']['JPY']))

        print("OK...")


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    exe = MainDialog()
    exe.show()
    try:
        sys.exit(app.exec())
    except SystemExit as e:
        print(f"정상적으로 마쳐야 할텐뎅..[{e}]")