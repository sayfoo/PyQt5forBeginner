import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from ui_plaintexteditTest import Ui_Dialog

class WindowClass(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #PlainTextEdit과 관련된 버튼에 기능 연결
        self.btn_printPlainTextEdit.clicked.connect(self.printPlainTextEdit)
        self.btn_clearPlainTextEdit.clicked.connect(self.clearPlainTextEdit)
        self.btn_appendPlainText.clicked.connect(self.appendPlainText)

    #PlainTextEdit과 관련된 함수
    def printPlainTextEdit(self) :
        print(self.plaintextedit_Test.toPlainText())

    def clearPlainTextEdit(self) :
        self.plaintextedit_Test.clear()

    def appendPlainText(self) :
        self.plaintextedit_Test.appendPlainText("Append Plain Text")

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    exe = WindowClass()
    exe.show()
    try:
        sys.exit(app.exec())
    except SystemExit as e:
        print(f"정상적으로 마쳐야 할텐뎅..[{e}]")