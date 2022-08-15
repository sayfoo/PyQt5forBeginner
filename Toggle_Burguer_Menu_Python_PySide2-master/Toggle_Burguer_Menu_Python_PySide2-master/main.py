################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
from functools import partial
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

# GUI FILE
from ui_ui_main_copy import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.text = {3: "5개 은하의 집합체 '스테판 5중주(Stephan Quintet)'의 모습",
                     1: "카리나 성운(Carina Nebula·용골자리 성운)의 모습",
                     2: "남쪽 고리 성운(Southern Ring Nebula)의 모습"}


        self.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))

        # self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_page_1.clicked.connect(partial(self.show_stacked_widgets, self.page_1, 1))

        # self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_2.clicked.connect(partial(self.show_stacked_widgets, self.page_2, 2))

        # self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_page_3.clicked.connect(partial(self.show_stacked_widgets, self.page_3, 3))

    def show_stacked_widgets(self, page, number):
        print(f"{page = }, {number = }")
        self.stackedWidget.setCurrentWidget(page)
        self.title_label.setText(self.text[number])


    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH

            width = self.frame_left_menu.width()
            print(f"enabled {maxWidth = } {width = }")
            maxExtend = maxWidth
            standard = 100

            # SET MAX WIDTH
            if width == 100:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(1000)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            # self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InElastic)
            self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
