import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QVBoxLayout

EXCHANGE_RATES = {
    'РУБЛЬ': 1,
    'ДОЛЛАР': 70,
    'ЕВРО': 80,
    'ЙЕНА': 0.6
}


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.message = QLabel(self)
        self.message.setText('Это программа для конвертации валют')
        self.layout().addWidget(self.message)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Converter.ui', self)
        self.input_type.addItems(EXCHANGE_RATES.keys())
        self.output_type.addItems(EXCHANGE_RATES.keys())
        self.pushButton.clicked.connect(self.convert)
        self.about_window = AboutWindow()
        self.about_action.triggered.connect(self.about)

    def about(self):
        self.about_window.show()

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATES[self.input_type.currentText()]
        output = input / EXCHANGE_RATES[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())