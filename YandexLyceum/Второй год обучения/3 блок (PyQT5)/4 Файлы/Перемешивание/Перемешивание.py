import sys
from mash import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Mixing(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mixing, self).__init__()
        self.setupUi(self)
        self.btn_load.clicked.connect(self.mixing_text)

    def mixing_text(self):
        self.text_browser.clear()
        try:
            with open('file.txt', encoding='utf8') as file:
                lines = file.readlines()
                self.text_browser.append(''.join(lines[1::2]))
                self.text_browser.append(''.join(lines[0::2]))
        except FileNotFoundError:
            self.statusBar().showMessage('Файл не найден')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mixing()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
