import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QCheckBox, QLineEdit


class Hide_Widgets(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 220, 200)
        self.setWindowTitle('Прятки для виджетов')

        x_cb, y_cb = 20, 30
        self.cb1 = QCheckBox('first', self)
        self.cb1.setChecked(True)
        self.cb1.move(x_cb, y_cb)
        self.cb1.stateChanged.connect(self.check)

        self.cb2 = QCheckBox('second', self)
        self.cb2.setChecked(True)
        self.cb2.move(x_cb, y_cb * 2)
        self.cb2.stateChanged.connect(self.check)

        self.cb3 = QCheckBox('third', self)
        self.cb3.setChecked(True)
        self.cb3.move(x_cb, y_cb * 3)
        self.cb3.stateChanged.connect(self.check)

        self.cb4 = QCheckBox('forth', self)
        self.cb4.setChecked(True)
        self.cb4.move(x_cb, y_cb * 4)
        self.cb4.stateChanged.connect(self.check)

        self.check_boxes = [self.cb1, self.cb2, self.cb3, self.cb4]
        text = "Hey, I'm here!"
        input_1 = QLineEdit(text, self)
        input_2 = QLineEdit(text, self)
        input_3 = QLineEdit(text, self)
        input_4 = QLineEdit(text, self)
        self.inputs = [input_1, input_2, input_3, input_4]
        start_x, start_y = 100, 30
        koef = 1
        for line in self.inputs:
            line.move(start_x, start_y * koef)
            koef += 1

    def check(self):
        for i in range(len(self.check_boxes)):
            if self.check_boxes[i].isChecked():
                self.inputs[i].show()
            else:
                self.inputs[i].hide()

def main():
    app = QApplication(sys.argv)
    ex = Hide_Widgets()
    ex.show()
    sys.exit(app.exec())


main()