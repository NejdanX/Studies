from PIL.ImageQt import ImageQt
from PIL import Image
import sys

from pil import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QTransform


class ImageOperation(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ImageOperation, self).__init__()
        self.setupUi(self)
        self.file_name = 'bbbb.jpg'
        self.new_image = 'new.jpg'
        self.angle = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PIL 2.0')
        self.pixmap = QPixmap(self.file_name)
        self.image_label.setPixmap(self.pixmap)

        self.btn_clockwise.clicked.connect(self.rotate)
        self.btn_counterclockwise.clicked.connect(self.rotate)

        self.btn_red.clicked.connect(self.choice_color)
        self.btn_green.clicked.connect(self.choice_color)
        self.btn_blue.clicked.connect(self.choice_color)
        self.btn_all.clicked.connect(self.choice_color)

    def rotate(self):
        sender = self.sender().text()
        if sender == 'По часовой стрелке':
            self.angle = (self.angle + 90) % 360
            self.image_label.setPixmap(self.pixmap.transformed(QTransform().rotate(self.angle)))
        else:
            self.angle = (self.angle - 90) % 360
            self.image_label.setPixmap(self.pixmap.transformed(QTransform().rotate(self.angle)))

    def choice_color(self):
        sender = self.sender().text()
        if sender == 'R':
            self.change_channel(0)
        elif sender == 'G':
            self.change_channel(1)
        elif sender == 'B':
            self.change_channel(2)
        else:
            self.change_channel(3)

    def change_channel(self, channel):
        self.im = Image.open(self.file_name)
        pixels = self.im.load()
        x, y = self.im.size
        for i in range(x):
            for j in range(y):
                if channel == 0:
                    pixels[i, j] = pixels[i, j][0], 0, 0
                elif channel == 1:
                    pixels[i, j] = 0, pixels[i, j][1], 0
                elif channel == 2:
                    pixels[i, j] = 0, 0, pixels[i, j][2]
                else:
                    break
        self.im.save(self.new_image)
        self.pixmap = QPixmap(self.new_image)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setPixmap(self.pixmap.transformed(QTransform().rotate(self.angle)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageOperation()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
