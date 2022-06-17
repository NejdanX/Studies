import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit


class Focus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 75)
        self.setWindowTitle('Фокус со словами')

        self.input_first = QLineEdit(self)
        self.input_first.resize(150, 30)
        self.input_first.move(20, 30)

        self.btn = QPushButton('->', self)
        self.btn.resize(30, 30)
        self.btn.move(180, 30)
        self.btn.clicked.connect(self.swap_input)

        self.input_second = QLineEdit(self)
        self.input_second.resize(150, 30)
        self.input_second.move(220, 30)

    def swap_input(self):
        old_first = self.input_first.text()
        self.input_first.setText(self.input_second.text())
        self.input_second.setText(old_first)
        self.btn.setText('->' if self.btn.text() == '<-' else '<-')


app = QApplication(sys.argv)
ex = Focus()
ex.show()
sys.exit(app.exec())