import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui_pushbutton import Ui_Dialog


class MyApp(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_01.clicked.connect(partial(self.button_clicked, "button 1"))
        self.btn_02.clicked.connect(partial(self.button_clicked, "button 2"))
        self.btn_03.clicked.connect(partial(self.button_clicked, "button 3"))
        self.btn_04.clicked.connect(partial(self.button_clicked, "button 4"))

        print(f"{partial(self.button_clicked, 'button 4').func = }")
        print(f"{partial(self.button_clicked, 'button 4').args = }")
        print(f"{partial(self.button_clicked, 'button 4').keywords = }")


    def button_clicked(self, value):
        print(f'{value} was clicked.')
        self.label.clear()
        self.label.setText(f'{value} was clicked.')
        self.label.setFont(QFont("Malgun Gothic", 20))
        self.label.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    exe = MyApp()
    exe.show()
    try:
        sys.exit(app.exec())
    except SystemExit as e:
        print(f"정상적으로 마쳐야 할텐뎅..[{e}]")