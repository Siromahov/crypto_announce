from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCheckBox, QPushButton
import sys

from info_edit import selected_info


class Coins(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 320, 200)
        self.setWindowTitle('Coins')
        self.display_images()
        self.display_labels()
        self.display_buttons()
        self.display_checkboxes()

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
        text.setText("Select crypro currencies:", )
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

    def display_checkboxes(self):
        BTC = QLabel(self)
        BTC.setWordWrap(True)

        BTC = QCheckBox('BTC', self)
        BTC.setStyleSheet("color : #66FCF1")
        BTC.setFont(QFont('calibri', 20))
        BTC.stateChanged.connect(self.print_selected)
        BTC.move(40, 50)

        ETH = QLabel(self)
        ETH.setWordWrap(True)

        ETH = QCheckBox('ETH', self)
        ETH.setStyleSheet("color : #66FCF1")
        ETH.setFont(QFont('calibri', 20))
        ETH.stateChanged.connect(self.print_selected)
        ETH.move(40, 80)

        LTC = QLabel(self)
        LTC.setWordWrap(True)

        LTC = QCheckBox('LTC', self)
        LTC.setStyleSheet("color : #66FCF1")
        LTC.setFont(QFont('calibri', 20))
        LTC.stateChanged.connect(self.print_selected)
        LTC.move(40, 110)

        HOT = QLabel(self)
        HOT.setWordWrap(True)

        HOT = QCheckBox('HOT', self)
        HOT.setStyleSheet("color : #66FCF1")
        HOT.setFont(QFont('calibri', 20))
        HOT.stateChanged.connect(self.print_selected)
        HOT.move(210, 50)

    def cancel(self):
        self.close()

    def print_selected(self, state, ):

        sender = self.sender()
        if state:
            currency = (format(sender.text()))
            selected_info.selected.append(currency)

        else:
            currency = (format(sender.text()))
            selected_info.selected.append(currency)

    def click_method(self):
        print(selected_info.all)

        self.cancel()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Coins()
    sys.exit(app.exec_())
