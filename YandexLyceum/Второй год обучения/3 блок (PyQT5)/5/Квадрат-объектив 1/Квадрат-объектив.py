import sys
from form import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Square(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Square, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Квадрат-объектив')
        self.do_paint = False
        self.image_label.setText('')
        self.btn_draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_square(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_square(self, qp):
        qp.setPen(QColor(255, 0, 0))
        x, y = 30, 100
        side = int(self.input_side.text())
        for i in range(int(self.input_count.text())):
            qp.drawRect(x, y, side, side)
            rever = 1 - float(self.input_coeff.text())
            side *= float(self.input_coeff.text())
            x, y = x, y
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square()
    ex.show()
    sys.exit(app.exec())