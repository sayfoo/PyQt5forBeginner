import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui_labelTest import Ui_Dialog

class WindowClass(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.toggle = 1

        #버튼에 기능을 할당하는 코드
        self.btn_changeText.clicked.connect(self.changeTextFunction)
        self.btn_printText.clicked.connect(self.printTextFunction)

    def changeTextFunction(self) :
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드
        if self.toggle == 1:
            self.lbl_Test.setText("안녕하세요. 덥죠...")
            self.toggle *= -1
        else:
            self.lbl_Test.setText("아뇨. 시원한 도서관입니당.")
            self.toggle *= -1
        self.lbl_Test.setAlignment(Qt.AlignCenter)

    def printTextFunction(self) :
        #self.Label이름.text()
        #Label에 있는 글자를 가져오는 메서드
        print(self.lbl_Test.text())

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
