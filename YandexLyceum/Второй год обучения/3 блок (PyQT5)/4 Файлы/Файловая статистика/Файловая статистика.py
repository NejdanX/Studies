import sys

from Statistic import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class FileStatistics(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FileStatistics, self).__init__()
        self.setupUi(self)
        self.btn_calculate.clicked.connect(self.find_statistics)

    def calculate_statistics(self, file):
        length = amount = minimum = maximum = 0
        for number in file.readlines():
            number = int(number)
            if maximum < number:
                if maximum == 0:
                    minimum = number
                maximum = number
            if minimum > number:
                minimum = number
            length += 1
            amount += number
        return maximum, minimum, amount / length

    def find_statistics(self):
        try:
            with open(self.input_file.text(), encoding='utf8') as f:
                statistics = self.calculate_statistics(f)
                self.statusBar().clearMessage()
                self.output_max.setText(str(statistics[0]))
                self.output_min.setText(str(statistics[1]))
                self.output_mean.setText(str(round(statistics[2], 3)))
                with open('output.txt', 'w', encoding='utf8') as f_w:
                    for elem in statistics:
                        f_w.write(str(elem) + '\n')
        except FileNotFoundError as error:
            self.statusBar().showMessage(f"В директории нет файла с именем '{self.input_file.text()}'")
        except ZeroDivisionError:
            self.statusBar().showMessage(f"Файл '{self.input_file.text()}' пуст")
        except ValueError as error:
            self.statusBar().showMessage(f"В файле '{self.input_file.text()}' содержаться некорректные данные")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStatistics()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
