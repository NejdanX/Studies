import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QTextBrowser, QHBoxLayout
from random import choice


class RandomString(QWidget):
    def __init__(self):
        super(RandomString, self).__init__()
        self.initUI()
        with open('cyrillic.txt', 'r', encoding='utf8') as f:
            self.ls = f.readlines()

    def initUI(self):
        main_layout = QHBoxLayout(self)

        self.btn_take_string = QPushButton('Получить', self)
        self.btn_take_string.clicked.connect(self.get_string)
        main_layout.addWidget(self.btn_take_string)

        self.text_editer = QTextBrowser(self)
        main_layout.addWidget(self.text_editer)

    def get_string(self):
        self.text_editer.append(choice(self.ls))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())
