import sys

from PyQt5.QtWidgets import QApplication, QLCDNumber, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 450, 200)
        self.setWindowTitle('Миникалькулятор')

        self.lbl_1 = QLabel(self)
        self.lbl_1.setText('Введите 1-ое число')
        self.lbl_1.adjustSize()
        self.lbl_1.move(20, 10)

        self.input_first = QLineEdit(self)
        self.input_first.resize(150, 30)
        self.input_first.move(20, 30)

        self.btn = QPushButton('->', self)
        self.btn.resize(50, 30)
        self.btn.move(200, 70)
        self.btn.clicked.connect(self.calculate)

        self.lbl_2 = QLabel(self)
        self.lbl_2.setText('Введите 2-ое число')
        self.lbl_2.adjustSize()
        self.lbl_2.move(20, 100)

        self.input_second = QLineEdit(self)
        self.input_second.resize(150, 30)
        self.input_second.move(20, 120)

        shift_x = 350
        self.amount = QLCDNumber(self)
        self.amount.move(shift_x, 10)
        self.for_amount = QLabel(self)
        self.for_amount.setText('Сумма:')
        self.for_amount.move(shift_x - 90, 15)
        self.for_amount.adjustSize()

        self.difference = QLCDNumber(self)
        self.difference.move(shift_x, 50)
        self.for_difference = QLabel(self)
        self.for_difference.setText('Разность:')
        self.for_difference.move(shift_x - 90, 55)
        self.for_difference.adjustSize()

        self.multiplication = QLCDNumber(self)
        self.multiplication.move(shift_x, 90)
        self.for_multiplication = QLabel(self)
        self.for_multiplication.setText('Произведение:')
        self.for_multiplication.move(shift_x - 90, 95)
        self.for_multiplication.adjustSize()

        self.division = QLCDNumber(self)
        self.division.move(shift_x, 130)
        self.for_division = QLabel(self)
        self.for_division.setText('Частное:')
        self.for_division.move(shift_x - 90, 135)
        self.for_division.adjustSize()

    def calculate(self):
        first_number, second_number = float(self.input_first.text()), float(self.input_second.text())
        self.amount.display(first_number + second_number)
        self.difference.display(first_number - second_number)
        self.multiplication.display(first_number * second_number)
        self.division.display(first_number / second_number if second_number else 'error')


app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec())