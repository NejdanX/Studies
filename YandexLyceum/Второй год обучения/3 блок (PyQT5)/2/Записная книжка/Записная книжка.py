from book_phone import Ui_MainWindow
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class Notebook(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Notebook, self).__init__()
        self.setupUi(self)
        self.btn_add.clicked.connect(self.add_note)

    def add_note(self):
        name, phone = self.input_name.text(), self.input_phone.text()
        self.phone_book.addItem(name + ' ' + phone)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())