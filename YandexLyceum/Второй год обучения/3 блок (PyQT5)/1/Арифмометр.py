import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class Arithmetic(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('арифмометр.ui', self)
        self.pushButton.clicked.connect(self.act)
        self.pushButton_2.clicked.connect(self.act)
        self.pushButton_3.clicked.connect(self.act)

    def act(self):
        first_number, second_number = int(self.lineEdit.text()), int(self.lineEdit_2.text())
        if self.sender().text() == '+':
            self.lineEdit_3.setText(str(first_number + second_number))
        elif self.sender().text() == '-':
            self.lineEdit_3.setText(str(first_number - second_number))
        else:
            self.lineEdit_3.setText(str(first_number * second_number))


def main():
    app = QApplication(sys.argv)
    ex = Arithmetic()
    ex.show()
    sys.exit(app.exec())


main()