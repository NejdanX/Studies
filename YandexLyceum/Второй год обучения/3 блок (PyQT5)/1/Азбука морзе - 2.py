import sys

from PyQt5.QtWidgets import QPushButton, QMainWindow, QLineEdit, QApplication


class Morse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 300, 100)
        self.setWindowTitle('Morse')

        x_start, y_start = 10, 10
        for i in range(26):
            self.button = QPushButton(chr(ord('a') + i), self)
            self.button.move(x_start, y_start)
            self.button.resize(20, 20)
            x_start += 20
            if i == 12:
                y_start += 30
                x_start = 10
            self.button.clicked.connect(self.translate)

        self.input = QLineEdit(self)
        self.input.move(10, 70)
        self.input.resize(260, 20)

    def translate(self):
        MORSE = {'a': '.-',
                 'b': '-...',
                 'c': '-.-.',
                 'd': '-..',
                 'e': '.',
                 'f': '..-.',
                 'g': '--.',
                 'h': '....',
                 'i': '..',
                 'j': '.---',
                 'k': '-.-',
                 'l': '.-..',
                 'm': '--',
                 'n': '-.',
                 'o': '---',
                 'p': '.--.',
                 'q': '--.-',
                 'r': '.-.',
                 's': '...',
                 't': '-',
                 'u': '..-',
                 'v': '...-',
                 'w': '.--',
                 'x': '-..-',
                 'y': '-.--',
                 'z': '--..'
                 }
        self.input.setText(self.input.text() + MORSE[self.sender().text()])


def main():
    app = QApplication(sys.argv)
    ex = Morse()
    ex.show()
    sys.exit(app.exec())


main()
