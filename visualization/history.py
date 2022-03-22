from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys

from info_edit import selected_info


class History(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 320, 250)
        self.setWindowTitle('History')
        self.display_images()
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
        text = QLabel(self)
        text.setText("History:")
        text.setFont(QFont('calibri', 20))
        text.setStyleSheet("color : #66FCF1")
        text.move(10, 10)

        last_completed = QLabel(self)
        last_completed.setText("Commits:")
        last_completed.setFont(QFont('calibri', 20))
        last_completed.setStyleSheet("color : #66FCF1")
        last_completed.move(20, 50)

        if len(selected_info.commits) == 0:
            last_commit = QLabel(self)
            last_commit.setText("No commits yet!")
            last_commit.setFont(QFont('calibri', 20))
            last_commit.setStyleSheet("color : #66FCF1")
            last_commit.move(40, 80)
        else:
            last_commit = QLabel(self)
            last_commit.setText(selected_info.commits[-1])
            last_commit.setFont(QFont('calibri', 20))
            last_commit.setStyleSheet("color : #66FCF1")
            last_commit.move(40, 80)

        last_completed = QLabel(self)
        last_completed.setText("Last committed(time):")
        last_completed.setFont(QFont('calibri', 20))
        last_completed.setStyleSheet("color : #66FCF1")
        last_completed.move(20, 120)

        if len(selected_info.commits) == 0:
            last_commit = QLabel(self)
            last_commit.setText("No commits yet!")
            last_commit.setFont(QFont('calibri', 20))
            last_commit.setStyleSheet("color : #66FCF1")
            last_commit.move(40, 150)
        else:
            last_commit = QLabel(self)
            last_commit.setText(selected_info.commits[-1])
            last_commit.setFont(QFont('calibri', 20))
            last_commit.setStyleSheet("color : #66FCF1")
            last_commit.move(40, 150)


    def display_buttons(self):
        exit_button = QPushButton("Exit", self)
        exit_button.setFont(QFont('calibri', 20))
        exit_button.setStyleSheet("background-color : #C5C6C7")
        exit_button.clicked.connect(self.exit)
        exit_button.setGeometry(200, 200, 90, 30)

    def on_changed(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = History()
    sys.exit(app.exec_())
