import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class TextFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag.ui', self)
        self.flags = ['', '', '']
        for i in range(self.vLayout_1.count()):
            self.vLayout_1.itemAt(i).widget().toggled.connect(self.set_flag)
            self.vLayout_2.itemAt(i).widget().toggled.connect(self.set_flag)
            self.vLayout_3.itemAt(i).widget().toggled.connect(self.set_flag)
        self.btn_print.clicked.connect(self.print_flag)

    def set_flag(self):
        for i in range(self.vLayout_1.count()):
            if self.vLayout_1.itemAt(i).widget().isChecked():
                self.flags[0] = self.vLayout_1.itemAt(i).widget().text()
            if self.vLayout_2.itemAt(i).widget().isChecked():
                self.flags[1] = self.vLayout_2.itemAt(i).widget().text()
            if self.vLayout_3.itemAt(i).widget().isChecked():
                self.flags[2] = self.vLayout_3.itemAt(i).widget().text()

    def print_flag(self):
        self.label_4.setText('Цвета: ' + ', '.join(self.flags))
        self.label_4.adjustSize()



def main():
    app = QApplication(sys.argv)
    ex = TextFlag()
    ex.show()
    sys.exit(app.exec())


main()
