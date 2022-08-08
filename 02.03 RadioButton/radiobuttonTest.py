import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui_radiobuttonTest import Ui_Dialog

class WindowClass(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        print(f"{sys.version}")

        #GroupBox안에 있는 RadioButton들을 연결합니다.
        #GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.
        self.groupBox_rad1.clicked.connect(partial(self.groupboxRadFunction, 1))
        self.groupBox_rad2.clicked.connect(partial(self.groupboxRadFunction, 2))
        self.groupBox_rad3.clicked.connect(partial(self.groupboxRadFunction, 3))
        self.groupBox_rad4.clicked.connect(partial(self.groupboxRadFunction, 4))

    def groupboxRadFunction(self, button):
        print(f"Group Box Button {button} is checked.")

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