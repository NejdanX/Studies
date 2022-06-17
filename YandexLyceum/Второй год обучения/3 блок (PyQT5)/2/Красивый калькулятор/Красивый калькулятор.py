import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from math import sqrt, factorial


class BeautifulCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.initUI()
        self.numbers = []
        self.operations = {'+': lambda x, y: x + y,
                           '-': lambda x, y: x - y,
                           '*': lambda x, y: x * y,
                           '/': lambda x, y: x / y,
                           '^': lambda x, y: x ** y
                           }
        self.number_for_display = ''

    def initUI(self):
        self.setWindowTitle('Beautiful Calculator')
        for digit in self.buttonGroup_digits.buttons():
            digit.clicked.connect(self.set_number)
        self.btn_dot.clicked.connect(self.set_number)
        for binary_operation in self.buttonGroup_binary.buttons():
            binary_operation.clicked.connect(self.binary_operation)
        self.btn_eq.clicked.connect(self.calculate)
        self.btn_fact.clicked.connect(self.do_unary_operation)
        self.btn_sqrt.clicked.connect(self.do_unary_operation)
        self.btn_clear.clicked.connect(self.clear)

    def set_number(self):
        self.number_for_display += self.sender().text()
        self.table.display(self.number_for_display)

    def binary_operation(self):
        self.numbers.append(self.table.value())
        self.numbers.append(self.sender().text())
        self.clear()

    def do_unary_operation(self):
        value = self.table.value()
        self.clear()
        operation = self.sender().text()
        if operation == '√':
            if value < 0:
                self.table.display('Error')
            else:
                self.table.display(sqrt(value))
        elif operation == '!':
            self.table.display(factorial(int(value)))

    def calculate(self):
        value = self.table.value()
        self.clear()
        if len(self.numbers) == 2:
            self.table.display(self.operations[self.numbers[1]](self.numbers[0], value))
        else:
            self.table.display('Error')
        self.numbers.clear()

    def clear(self):
        self.number_for_display = ''
        self.table.display('')

def main():
    app = QApplication(sys.argv)
    ex = BeautifulCalculator()
    ex.show()
    sys.exit(app.exec())


main()
