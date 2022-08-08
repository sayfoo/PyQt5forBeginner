import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui_checkboxTest import Ui_Dialog


class WindowClass(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #GroupBox밖에 있는 CheckBox에 기능 연결
        self.chk_1.stateChanged.connect(self.chkFunction)
        self.chk_2.stateChanged.connect(self.chkFunction)
        self.chk_3.stateChanged.connect(self.chkFunction)
        self.chk_4.stateChanged.connect(self.chkFunction)

        #GroupBox안에 있는 CheckBox에 기능 연결
        self.groupchk_1.stateChanged.connect(self.groupchkFunction)
        self.groupchk_2.stateChanged.connect(self.groupchkFunction)
        self.groupchk_3.stateChanged.connect(self.groupchkFunction)
        self.groupchk_4.stateChanged.connect(self.groupchkFunction)

    def chkFunction(self):
        #CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if self.chk_1.isChecked() : print("chk_1 isChecked")
        if self.chk_2.isChecked() : print("chk_2 isChecked")
        if self.chk_3.isChecked() : print("chk_3 isChecked")
        if self.chk_4.isChecked() : print("chk_4 isChecked")

    def groupchkFunction(self):
        #CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if self.groupchk_1.isChecked() : print("groupchk_1 isChecked")
        if self.groupchk_2.isChecked() : print("groupchk_2 isChecked")
        if self.groupchk_3.isChecked() : print("groupchk_3 isChecked")
        if self.groupchk_4.isChecked() : print("groupchk_4 isChecked")


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