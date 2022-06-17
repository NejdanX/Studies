import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout
MATRIX = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

class WidgetArt(QWidget):
    def __init__(self):
        super(WidgetArt, self).__init__()
        self.initUI()

    def initUI(self):
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        for i in range(len(MATRIX)):
            for j in range(len(MATRIX[i])):
                check = QCheckBox(self)
                check.setChecked(MATRIX[i][j])
                check.setEnabled(MATRIX[i][j])
                self.main_layout.addWidget(check, i, j)
        self.move(300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetArt()
    ex.show()
    sys.exit(app.exec_())