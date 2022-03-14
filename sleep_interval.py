from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCheckBox, QPushButton, QTextEdit
import sys

import selected_info


class sleep_interval(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 320, 200)
        self.setWindowTitle('Sleep interval')
        self.display_images()
        self.display_labels()
        self.display_buttons()
        self.display_textbox()

        self.show()

    def display_images(self):
        background_image = "img/grey2.png"
        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found.")

    def display_labels(self):
        text = QLabel(self)
        text.setText("Select sleep interval:", )
        text.setFont(QFont('calibri', 20))
        text.setStyleSheet("color : #66FCF1")
        text.move(10, 10)

    def display_buttons(self):
        cancel_button = QPushButton("Cancel", self)
        cancel_button.setFont(QFont('calibri', 20))
        cancel_button.setStyleSheet("background-color : #C5C6C7")
        cancel_button.clicked.connect(self.cancel)
        cancel_button.setGeometry(30, 155, 90, 30)

        save_button = QPushButton("Save", self)
        save_button.setFont(QFont('calibri', 20))
        save_button.setStyleSheet("background-color : #C5C6C7")
        save_button.clicked.connect(self.click_method)
        save_button.setGeometry(200, 155, 90, 30)

    def display_textbox(self):
        self.hour = QTextEdit("Hour: ", self)
        self.hour.resize(200, 30)
        self.hour.setFont(QFont('calibri', 12))
        self.hour.move(10, 55)

        self.minute = QTextEdit("Minute: ", self)
        self.minute.resize(200, 30)
        self.minute.setFont(QFont('calibri', 12))
        self.minute.move(10, 100)

    def cancel(self):
        self.close()

    def click_method(self):
        hour_value = self.hour.toPlainText()
        minute_value = self.minute.toPlainText()
        selected_info.hour = hour_value + selected_info.hour
        selected_info.minute = minute_value + selected_info.minute
        print(selected_info.all)

        self.cancel()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = sleep_interval()
    sys.exit(app.exec_())
