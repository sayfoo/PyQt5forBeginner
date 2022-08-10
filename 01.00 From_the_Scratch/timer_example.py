import sys
from PySide6.QtWidgets import QApplication, QWidget, QLCDNumber
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTimer, QDateTime, QTime
# from ui_timer_example import Ui_Form
# from ui_lcd_example import Ui_Form
from ui_splitter_example import Ui_Form


class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.datetime = QDateTime()
        self.timer = QTimer()
        self.disp_clock.setDigitCount(8)
        self.total_splitter.setSizes([200, 548])
        self.hide = False       #
        # self.setup_datetime()

        self.timer.timeout.connect(self.display_datetime)
        self.start_btn.clicked.connect(self.start_datetime)
        self.stop_btn.clicked.connect(self.stop_datetime)
        self.hide_btn.clicked.connect(self.toggle_left_image)


    def setup_datetime(self):
        self.current_time = self.datetime.currentDateTime()
        self.display = self.current_time.toString("yyyy-MM-dd hh:mm:ss dddd")
        print(f"{self.display = }")
        print(f"{self.disp_label.font() = }")
        self.disp_label.setText(self.display)

    def display_datetime(self):
        self.current_time = self.datetime.currentDateTime()
        self.display = self.current_time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.disp_label.setText(self.display)

        self.clock = self.display.split()[1] # time only
        self.disp_clock.display(self.clock)

    def toggle_left_image(self):
        if not self.hide:
            self.total_splitter.setSizes([200, 548])
            self.frame.setVisible(True)
            print("hide")
            self.hide = True
        else:
            self.total_splitter.setSizes([0, 548])
            self.frame.setVisible(False)
            print("show")
            self.hide = False

    def start_datetime(self):
        self.timer.start(1000)
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

        self.frame_01.setVisible(False)
        self.frame_02.setVisible(True)
        self.frame.setVisible(False)
        self.hide = False
        # self.frame_02.setHidden(False)


    def stop_datetime(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

        self.frame_01.setVisible(True)
        self.frame_02.setVisible(True)

        self.frame.setVisible(True)
        self.hide = True
        # self.frame_02.setHidden(True)


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
        print(f"잘 되어야 할 텐뎅...[{e}]")