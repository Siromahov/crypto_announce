from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QTextEdit, QComboBox, QHBoxLayout
import sys


class night_mode(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 320, 250)
        self.setWindowTitle('Night mode')
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
        text.setText("Night mode:", )
        text.setFont(QFont('calibri', 20))
        text.setStyleSheet("color : #66FCF1")
        text.move(10, 10)

        from_ = QLabel(self)
        from_.setText("From:", )
        from_.setFont(QFont('calibri', 15))
        from_.setStyleSheet("color : #66FCF1")
        from_.move(30, 50)

        from_ = QLabel(self)
        from_.setText("To:", )
        from_.setFont(QFont('calibri', 15))
        from_.setStyleSheet("color : #66FCF1")
        from_.move(30, 115)

    def display_buttons(self):
        cancel_button = QPushButton("Cancel", self)
        cancel_button.setFont(QFont('calibri', 20))
        cancel_button.setStyleSheet("background-color : #C5C6C7")
        cancel_button.clicked.connect(self.cancel)
        cancel_button.setGeometry(30, 200, 90, 30)

        save_button = QPushButton("Save", self)
        save_button.setFont(QFont('calibri', 20))
        save_button.setStyleSheet("background-color : #C5C6C7")
        save_button.setGeometry(200, 200, 90, 30)

    def display_textbox(self):
        self.hour_field = QTextEdit("Hour: ", self)
        self.hour_field.setFont(QFont('calibri', 12))
        self.hour_field.setGeometry(30, 75, 150, 30)

        self.combo = QComboBox(self)
        self.combo.setStyleSheet("background-color : #C5C6C7")
        self.combo.setFont(QFont('calibri', 15))
        self.combo.setGeometry(200, 75, 90, 30)

        self.combo.addItem("Am")
        self.combo.addItem("Pm")

        self.hour_field = QTextEdit("Hour: ", self)
        self.hour_field.setFont(QFont('calibri', 12))
        self.hour_field.setGeometry(30, 140, 150, 30)

        self.combo = QComboBox(self)
        self.combo.setStyleSheet("background-color : #C5C6C7")
        self.combo.setFont(QFont('calibri', 15))
        self.combo.setGeometry(200, 140, 90, 30)

        self.combo.addItem("Am")
        self.combo.addItem("Pm")



        self.label = QLabel(self)
        self.label.move(90, 40)

        self.combo.activated[str].connect(self.on_changed)

    def on_changed(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

    def cancel(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = night_mode()
    sys.exit(app.exec_())
