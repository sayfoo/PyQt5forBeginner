import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap

from ui_menu import Ui_MainWindow


class myMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        print(f"{self.splitter.sizes() = }")

        # =====================================================================================================
        # initialize elements
        self.cars_widget = self.carsWidget
        self.social_media_widget = self.socialWidget

        self.home_btn = self.pushButton
        self.toyota_btn = self.pushButton_3
        self.lexus_btn = self.pushButton_4
        self.mazda_btn = self.pushButton_8

        self.youtube_btn = self.pushButton_6
        self.tumblr_btn = self.pushButton_7

        self.logo_label = self.logoImg_2
        self.title_label = self.companyName_2

        # =====================================================================================================
        # create dict for all the function buttons
        self.menu_buttons = {
            self.home_btn: {
                "btn": self.home_btn,
                "icon_path": "icons/home-4-48.ico",
                "index": 0
            },
            self.toyota_btn: {
                "btn": self.toyota_btn,
                "icon_path": "icons/toyota-48.ico",
                "index": 1
            },
            self.lexus_btn: {
                "btn": self.lexus_btn,
                "icon_path": "icons/lexus-48.ico",
                "index": 2
            },
            self.mazda_btn: {
                "btn": self.mazda_btn,
                "icon_path": "icons/mazda-48.ico",
                "index": 3
            },
            self.youtube_btn: {
                "btn": self.youtube_btn,
                "icon_path": "icons/youtube-3-48.ico",
                "index": 4
            },
            self.tumblr_btn: {
                "btn": self.tumblr_btn,
                "icon_path": "icons/tumblr-3-48.ico",
                "index": 5
            },
            self.actionToyota: {
                "btn": self.toyota_btn,
                "icon_path": "icons/toyota-48.ico",
                "index": 1
            },
            self.actionLexus: {
                "btn": self.lexus_btn,
                "icon_path": "icons/lexus-48.ico",
                "index": 2
            },
            self.actionMazda: {
                "btn": self.mazda_btn,
                "icon_path": "icons/mazda-48.ico",
                "index": 3
            },
            self.actionYouTube: {
                "btn": self.youtube_btn,
                "icon_path": "icons/youtube-3-48.ico",
                "index": 4
            },
            self.actionTumblr: {
                "btn": self.tumblr_btn,
                "icon_path": "icons/tumblr-3-48.ico",
                "index": 5
            },
        }

        # =====================================================================================================
        # hide menu widget when start app
        self.cars_widget.hide()
        self.social_media_widget.hide()

        # =====================================================================================================
        # initialize home page button when start app
        self.home_btn.setDisabled(True)
        self.home_btn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.home_btn.setStyleSheet("color: rgb(0, 0, 0);")

        # =====================================================================================================
        # connect buttons with function
        self.action_Exit.triggered.connect(self.close)

        self.home_btn.clicked.connect(self.do_change_window)

        self.toyota_btn.clicked.connect(self.do_change_window)
        self.lexus_btn.clicked.connect(self.do_change_window)
        self.mazda_btn.clicked.connect(self.do_change_window)

        self.youtube_btn.clicked.connect(self.do_change_window)
        self.tumblr_btn.clicked.connect(self.do_change_window)

        self.actionToyota.triggered.connect(self.do_change_window)
        self.actionLexus.triggered.connect(self.do_change_window)
        self.actionMazda.triggered.connect(self.do_change_window)

        self.actionYouTube.triggered.connect(self.do_change_window)
        self.actionTumblr.triggered.connect(self.do_change_window)
        # print(f"{self.TextEnable = }\t{self.split.sizes() = }")

    def do_change_window(self):
        """
        for showing page in window
        """
        # =====================================================================================================
        # get clicked button signal
        print(f"{self.splitter.sizes() = }")
        button = self.sender()


        # =====================================================================================================
        # get button information from button dict
        clicked_btn_info = self.menu_buttons[button]

        # =====================================================================================================
        # set page title and icon
        self.title_label.setText(clicked_btn_info['btn'].text().strip())
        pixmap = QPixmap(clicked_btn_info['icon_path'])
        self.logo_label.setPixmap(pixmap)

        # =====================================================================================================
        # change button status for all the buttons
        for value in self.menu_buttons.values():
            if value['btn'] == clicked_btn_info['btn']:
                # =============================================================================================
                # change button status to disabled. set font and background color.
                clicked_btn_info['btn'].setDisabled(True)
                clicked_btn_info['btn'].setStyleSheet("background-color: rgb(222, 222, 222);")
                clicked_btn_info['btn'].setStyleSheet("color: rgb(0, 0, 0);")

                # ============================================================================================
                # set the page wanted to show
                self.stackedWidget.setCurrentIndex(value['index'])

            else:
                value['btn'].setDisabled(False)
                value['btn'].setStyleSheet("background-color: white;")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = myMainWindow()
    window.show()

    sys.exit(app.exec())
