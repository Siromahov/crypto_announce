from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCheckBox, QPushButton
import sys

import night_mode
import add_new_email
import sleep_interval
import coins

right_buttons_x_axis = 300
left_buttons_x_axis = 30
mails = ["vasilsonicsiromahov@gmail.com"]


class control_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 410, 240)
        self.setWindowTitle('Crypto announce')
        self.display_images()
        self.display_labels()
        self.display_buttons()
        self.display_checkboxes()
        self.add_new_email()

        self.show()

    def display_images(self):
        background_image = "img/grey.png"
        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found.")

    def display_labels(self):
        text = QLabel(self)
        text.setText("Send to:", )
        text.setFont(QFont('calibri', 20))
        text.setStyleSheet("color : #66FCF1")
        text.move(10, 70)

    def display_checkboxes(self):
        header_label = QLabel(self)
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)

        email = QCheckBox(mails[0], self)
        email.setStyleSheet("color : #66FCF1")
        email.setFont(QFont('calibri', 12))
        email.move(left_buttons_x_axis, 110)

    def display_buttons(self):

        start_button = QPushButton("Start", self)
        start_button.setFont(QFont('calibri', 20))
        start_button.setStyleSheet("background-color : #C5C6C7")
        start_button.setGeometry(300, 10, 100, 30)
        start_button.move(50, 20)

        add_new_button = QPushButton("Add new account", self)
        add_new_button.setStyleSheet("background-color : #C5C6C7")
        add_new_button.clicked.connect(self.add_new_email)
        add_new_button.setFont(QFont('calibri', 12))
        add_new_button.setGeometry(300, 10, 140, 30)
        add_new_button.move(left_buttons_x_axis, 200)

        pause_button = QPushButton("Pause", self)
        pause_button.setFont(QFont('calibri', 20))
        pause_button.setStyleSheet("background-color : #C5C6C7")
        pause_button.setGeometry(300, 10, 90, 30)
        pause_button.move(260, 20)

        sleep_interval_button = QPushButton("Sleep Interval", self)
        sleep_interval_button.setFont(QFont('calibri', 12))
        sleep_interval_button.setStyleSheet("background-color : #C5C6C7")
        sleep_interval_button.clicked.connect(self.sleep_interval)
        sleep_interval_button.setGeometry(300, 10, 100, 30)
        sleep_interval_button.move(right_buttons_x_axis, 80)

        coins_choice_button = QPushButton("   Coins   ", self)
        coins_choice_button.setFont(QFont('calibri', 12))
        coins_choice_button.setStyleSheet("background-color : #C5C6C7")
        coins_choice_button.clicked.connect(self.coins)
        coins_choice_button.setGeometry(300, 10, 100, 30)
        coins_choice_button.move(right_buttons_x_axis, 120)

        night_mode_button = QPushButton("Night mode", self)
        night_mode_button.setFont(QFont('calibri', 12))
        night_mode_button.setStyleSheet("background-color : #C5C6C7")
        night_mode_button.clicked.connect(self.night_mode)
        night_mode_button.setGeometry(300, 10, 100, 30)
        night_mode_button.move(right_buttons_x_axis, 160)

        restore_button = QPushButton("   Restore   ", self)
        restore_button.setFont(QFont('calibri', 12))
        restore_button.setStyleSheet("background-color : #C5C6C7")
        restore_button.setGeometry(300, 10, 100, 30)
        restore_button.move(right_buttons_x_axis, 200)

    def add_new_email(self):
        self.w = add_new_email.add_new_email()
        self.w.show()

    def night_mode(self):
        self.w = night_mode.night_mode()
        self.w.show()

    def sleep_interval(self):
        self.w = sleep_interval.sleep_interval()
        self.w.show()

    def coins(self):
        self.w = coins.coins()
        self.w.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = control_window()
    sys.exit(app.exec_())
