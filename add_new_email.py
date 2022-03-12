from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QTextEdit
import sys

import visualization

right_buttons_x_axis = 300
left_buttons_x_axis = 20


class add_new_email(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):

        self.setGeometry(100, 100, 320, 200)
        self.setWindowTitle('Add new email')

        self.display_images()
        self.display_textbox()
        self.display_labels()
        self.display_buttons()

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

        text_label = QLabel(self)
        text_label.setText("Add new account:", )
        text_label.setFont(QFont('calibri', 20))
        text_label.setStyleSheet("color : #66FCF1")
        text_label.move(10, 10)

    def display_textbox(self):

        self.text_field = QTextEdit(self)
        self.text_field.resize(300, 30)
        self.setFont(QFont('calibri', 12))
        self.text_field.move(10, 60)

    def display_buttons(self):

        cancel_button = QPushButton("Cancel", self)
        cancel_button.setFont(QFont('calibri', 20))
        cancel_button.setStyleSheet("background-color : #C5C6C7")
        cancel_button.clicked.connect(self.cancel)
        cancel_button.setGeometry(30, 120, 90, 30)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.click_method)
        save_button.setFont(QFont('calibri', 20))
        save_button.setStyleSheet("background-color : #C5C6C7")
        save_button.setGeometry(200, 120, 90, 30)

    def cancel(self):
        self.close()

    def click_method(self):
        mail = self.text_field.toPlainText()
        print(mail)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = add_new_email()
    sys.exit(app.exec_())
