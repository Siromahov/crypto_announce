from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCheckBox, QPushButton, QMessageBox
import sys

import selected_info
import add_new_email
import sleep_interval
import coins
import night_mode

right_buttons_x_axis = 300
left_buttons_x_axis = 30

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
        self.display_start_button()

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

    def display_start_button(self):

        start_button = QPushButton("Start", self)
        start_button.setFont(QFont('calibri', 20))
        start_button.setStyleSheet("background-color : #C5C6C7")
        start_button.clicked.connect(self.start)
        start_button.setGeometry(50, 20, 100, 30)

    def display_labels(self):
        text = QLabel(self)
        text.setText("Send to:", )
        text.setFont(QFont('calibri', 20))
        text.setStyleSheet("color : #66FCF1")
        text.setGeometry(10, 70, 100, 30)

    def display_checkboxes(self):
        header_label = QLabel(self)
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)

        email = QCheckBox("vasilsonicsiromahov@gmail.com", self)
        email.setStyleSheet("color : #66FCF1")
        email.setFont(QFont('calibri', 12))
        email.stateChanged.connect(self.selected_mail)
        email.move(left_buttons_x_axis, 110)

    def display_buttons(self):
        add_new_button = QPushButton("Add new account", self)
        add_new_button.setStyleSheet("background-color : #C5C6C7")
        add_new_button.clicked.connect(self.add_new_email)
        add_new_button.setFont(QFont('calibri', 12))
        add_new_button.setGeometry(30, 200, 140, 30)

        pause_button = QPushButton("Pause", self)
        pause_button.setFont(QFont('calibri', 20))
        pause_button.setStyleSheet("background-color : #C5C6C7")
        pause_button.setGeometry(260, 20, 90, 30)

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
        coins_choice_button.setGeometry(300, 120, 100, 30)

        night_mode_button = QPushButton("Night mode", self)
        night_mode_button.setFont(QFont('calibri', 12))
        night_mode_button.setStyleSheet("background-color : #C5C6C7")
        night_mode_button.clicked.connect(self.night_mode)
        night_mode_button.setGeometry(300, 160, 100, 30)

        restore_button = QPushButton("   Restore   ", self)
        restore_button.setFont(QFont('calibri', 12))
        restore_button.setStyleSheet("background-color : #C5C6C7")
        restore_button.setGeometry(300, 200, 100, 30)
        restore_button.clicked.connect(self.restore)

    def selected_mail(self, state):

        sender = self.sender()
        if state:
            mail = (format(sender.text()))
            selected_info.mails.append(mail)
            print(selected_info.all)
        else:
            selected_info.mails.clear()
            print(selected_info.all)

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

    def restore(self):
        selected_info.mails.clear()
        selected_info.hour.clear()
        selected_info.minute.clear()
        selected_info.selected.clear()
        print(selected_info.all)

    def start(self):
        if len(selected_info.mails) < 1:
            self.email_dialog()
        else:
            self.not_selected_crypto_currency()

    def not_selected_crypto_currency(self):
        if len(selected_info.selected) < 1:
            self.not_selected_crypto_currency_dialog()

        else:
            self.not_selected_sleep_interval()

    def not_selected_sleep_interval(self):
        if len(selected_info.hour) < 1 or len(selected_info.minute) < 1:
            self.time_dialog()
            print(selected_info.hour)
            import main
            main

        else:
            import main
            main

    def email_dialog(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText("Select at least one email to continue!")
        message.setWindowTitle("No email selected")
        message.setStandardButtons(QMessageBox.Ok)

        returnValue = message.exec()

    def time_dialog(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText("We will set the sleep interval by default to 1 hour!")
        message.setWindowTitle("Not defined sleep interval")
        message.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

        returnValue = message.exec()
        if returnValue == QMessageBox.Ok:
            selected_info.hour.append(hour)

            print(selected_info.all)

    def not_selected_crypto_currency_dialog(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText("Select at least one crypto currency to continue!")
        message.setWindowTitle("No currency selected")
        message.setStandardButtons(QMessageBox.Ok)

        returnValue = message.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = control_window()
    sys.exit(app.exec_())
