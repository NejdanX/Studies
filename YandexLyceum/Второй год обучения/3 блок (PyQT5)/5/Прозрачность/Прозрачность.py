import sys
from Slider import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QImage, QColor, qRed, qGreen, qBlue, qRgba
from PIL import Image


class Transparency(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Transparency, self).__init__()
        self.setupUi(self)
        self.file_name = 'bbbb.jpg'
        self.result_file = 'res.jpg'
        self.image = QImage(self.file_name)
        self.image = self.image.convertToFormat(QImage.Format_ARGB32)
        print(self.image.hasAlphaChannel())
        self.pixmap = QPixmap(self.file_name)
        self.label_image.setPixmap(self.pixmap)
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.change_transparency)

    def change_transparency(self):
        for i in range(self.image.width()):
            for j in range(self.image.height()):
                pixel = self.image.pixel(i, j)
                r, g, b = qRed(pixel), qGreen(pixel), qBlue(pixel)
                self.image.setPixel(i, j, qRgba(r, g, b, int(2.55 * self.slider.value())))
        self.label_image.setPixmap(QPixmap(self.image))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Transparency()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
