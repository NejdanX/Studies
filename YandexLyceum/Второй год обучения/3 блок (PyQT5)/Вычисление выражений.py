import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit


class CalculateStatement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 75)
        self.setWindowTitle('Вычисление выражений')

        self.input_first = QLineEdit(self)
        self.input_first.resize(150, 30)
        self.input_first.move(20, 30)

        self.btn = QPushButton('->', self)
        self.btn.resize(30, 30)
        self.btn.move(180, 30)
        self.btn.clicked.connect(self.calculate)

        self.input_second = QLineEdit(self)
        self.input_second.resize(150, 30)
        self.input_second.move(220, 30)

    def calculate(self):
        self.input_second.setText(str(eval(self.input_first.text())))


app = QApplication(sys.argv)
ex = CalculateStatement()
ex.show()
sys.exit(app.exec())