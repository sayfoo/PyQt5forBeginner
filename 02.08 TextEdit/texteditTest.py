import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from ui_texteditTest import Ui_Dialog


class WindowClass(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        #TextEdit과 관련된 버튼에 기능 연결
        self.btn_printTextEdit.clicked.connect(self.printTextEdit)
        self.btn_clearTextEdit.clicked.connect(self.clearTextEdit)
        self.btn_setFont.clicked.connect(self.settingFont)
        self.btn_setFontItalic.clicked.connect(self.fontItalic)
        self.btn_setFontColor.clicked.connect(self.fontColorRed)
        self.btn_fontSizeUp.clicked.connect(self.fontSizeUp)
        self.btn_fontSizeDown.clicked.connect(self.fontSizeDown)

    def printTextEdit(self) :
        print(self.textedit_Test.toPlainText())

    def clearTextEdit(self) :
        self.textedit_Test.clear()

    def settingFont(self) :
        fontvar = QFont("Malgun Gothic",10)
        self.textedit_Test.setCurrentFont(fontvar)
        self.textedit_Test.append("This is Text Edit\nThis widget support Rich Text")

    def fontItalic(self) :
        self.textedit_Test.setFontItalic(True)
        self.textedit_Test.append("This is Text Edit\nThis widget support Rich Text")

    def fontColorRed(self) :
        colorvar = QColor(255,0,0)
        self.textedit_Test.setTextColor(colorvar)
        self.textedit_Test.append("This is Text Edit\nThis widget support Rich Text")

    def fontSizeUp(self) :
        self.fontSize = self.fontSize + 1
        self.textedit_Test.setFontPointSize(self.fontSize)
        self.textedit_Test.append("This is Text Edit\nThis widget support Rich Text")

    def fontSizeDown(self) :
        self.fontSize = self.fontSize - 1
        self.textedit_Test.setFontPointSize(self.fontSize)
        self.textedit_Test.append("This is Text Edit\nThis widget support Rich Text")


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