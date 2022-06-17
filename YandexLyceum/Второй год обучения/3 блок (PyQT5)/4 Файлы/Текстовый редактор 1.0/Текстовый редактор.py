import sys

from FTextEditor import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class TextEditor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.setupUi(self)
        self.textBrowser.setReadOnly(False)
        self.btn_create.clicked.connect(self.create_new_file)
        self.btn_open.clicked.connect(self.open_file)
        self.btn_save.clicked.connect(self.save_file)

    def create_new_file(self):
        self.textBrowser.clear()
        open(self.input_file_name.text(), 'w', encoding='utf8').close()

    def open_file(self):
        try:
            with open(self.input_file_name.text(), 'r', encoding='utf8') as f:
                self.textBrowser.setText(f.read())
        except FileNotFoundError:
            self.statusBar().showMessage(f'Файл с именем {self.input_file_name} не найден')

    def save_file(self):
        with open(self.input_file_name.text(), 'w', encoding='utf8') as file:
            file.write(self.textBrowser.toPlainText())



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextEditor()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())