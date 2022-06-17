import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QComboBox
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy
from math import sqrt, factorial

EXCHANGE_RATES = {
    'РУБЛЬ': 1,
    'ДОЛЛАР': 70,
    'ЕВРО': 80,
    'ЙЕНА': 0.6
}



class BeautifulCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Конвертер валют')

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value = QLineEdit(self)
        self.input_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_type = QComboBox(self)
        self.input_type.addItems(EXCHANGE_RATES)
        self.input_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.convert_button = QPushButton(self)
        self.convert_button.setText('->')
        self.convert_button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setReadOnly(True)
        self.output_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_type = QComboBox(self)
        self.output_type.addItems(EXCHANGE_RATES)
        self.output_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_layout.addWidget(self.input_value)
        self.input_layout.addWidget(self.input_type)

        self.output_layout.addWidget(self.output_value)
        self.output_layout.addWidget(self.output_type)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.convert_button)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATES[self.input_type.currentText()]
        output = input / EXCHANGE_RATES[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')

def main():
    app = QApplication(sys.argv)
    ex = BeautifulCalculator()
    ex.show()
    sys.exit(app.exec())


main()
