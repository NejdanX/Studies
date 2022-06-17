import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Macdonalds(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Мак.ui', self)
        self.products = []
        for i in range(self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().stateChanged.connect(self.add_product)
        self.plainTextEdit.setReadOnly(True)
        self.pushButton.clicked.connect(self.order)

    def add_product(self):
        if self.sender().isChecked():
            self.products.append(self.sender().text())
        else:
            self.products.remove(self.sender().text())

    def order(self):
        self.plainTextEdit.document().setPlainText('Ваш заказ\n\n' + '\n'.join(self.products))


def main():
    app = QApplication(sys.argv)
    ex = Macdonalds()
    ex.show()
    sys.exit(app.exec())


main()
