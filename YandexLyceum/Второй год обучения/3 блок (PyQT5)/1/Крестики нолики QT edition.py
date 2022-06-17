import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import numpy as np


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Крестики-нолики.ui', self)
        self.initUI()

    def initUI(self):
        x_start, y_start = 50, 10
        self.buttons = []
        for i in range(9):
            if i % 3 == 0:
                y_start += 70
                x_start = 50
            self.button = QPushButton(self)
            self.button.move(x_start, y_start)
            self.button.resize(70, 70)
            self.buttons.append(self.button)
            self.button.clicked.connect(self.game)
            self.radioButton.toggled.connect(self.cross_or_zero)
            x_start += 70
        self.radioButton.setChecked(True)
        self.pushButton_10.clicked.connect(self.new_game)

    def cross_or_zero(self):
        self.state = 'X' if self.radioButton.isChecked() else 'O'

    def game(self):
        if self.sender().text():
            return
        self.sender().setText(self.state)
        result = self.check_winner()
        if result:
            self.label.setText(result)
            self.label.adjustSize()
            for button in self.buttons:
                button.setEnabled(False)
        self.state = 'X' if self.state == 'O' else 'O'

    def new_game(self):
        self.radioButton.setChecked(True)
        self.label.setText('')
        self.state = 'X'
        for button in self.buttons:
            button.setEnabled(True)
            button.setText('')


    def check_winner(self):
        self.array = np.array(self.buttons).reshape(3, 3)
        for i in range(3):
            for j in range(3):
                self.array[i][j] = self.array[i][j].text()
        winner = ''
        for i in range(3):
            if all(self.array[:, i] == self.state) or all(self.array[i] == self.state):
                winner = f'Выиграл {self.state}'
        if all(np.diagonal(self.array) == self.state) or all(np.diagonal(np.fliplr(self.array)) == self.state):
            winner = f'Выиграл {self.state}'
        if not winner and all(self.array[0]) and all(self.array[1]) and all(self.array[2]):
            winner = 'Ничья'
        return winner

def main():
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec())


main()