import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from planner import Ui_MainWindow


class Planner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.calendar.clicked.connect(self.get_date)
        self.btn_add.clicked.connect(self.add_note)

    def get_date(self):
        date = self.sender().selectedDate()
        self.year, self.month, self.day = date.year(), date.month(), date.day()

    def add_note(self):
        date = f'{str(self.year)}-{str(self.month).rjust(2, "0")}-{str(self.day).rjust(2, "0")}'
        time = self.time_edit.text()
        self.list_doings.addItem(date + ' ' + time + ' ' + self.input_doing.text())
        self.list_doings.sortItems()


def main():
    app = QApplication(sys.argv)
    ex = Planner()
    ex.show()
    sys.exit(app.exec())


main()