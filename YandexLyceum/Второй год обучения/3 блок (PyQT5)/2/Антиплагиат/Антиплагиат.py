from Antiplagiat import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Antiplagiarism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Antiplagiarism, self).__init__()
        self.setupUi(self)
        self.btn_check.clicked.connect(self.check_text)

    def check_text(self):
        strings_first_text = ' '.join(list(filter(lambda x: x, self.text_edit_1.toPlainText().split('\n')))).split()
        strings_second_text = ' '.join(list(filter(lambda x: x, self.text_edit_2.toPlainText().split('\n')))).split()
        if strings_first_text == strings_second_text:
            self.statusBar().setStyleSheet("background-color : red")
            self.statusbar.showMessage('Вероятность плагиата: 100.00%')
            return
        count_plag = 0
        if len(strings_first_text) <= len(strings_second_text):
            strings_first_text, strings_second_text = strings_second_text, strings_first_text
        for i in range(len(strings_first_text)):
            if strings_first_text[i] in strings_second_text:
                count_plag += 1
        if count_plag:
            plag_probability = (count_plag / len(strings_first_text)) * 100
            if plag_probability > self.input_threshold.value():
                self.statusBar().setStyleSheet("background-color : red")
            else:
                self.statusBar().setStyleSheet("background-color : green")
            self.statusbar.showMessage(f'Вероятность плагиата: {plag_probability:.2f}%')
        else:
            self.statusBar().setStyleSheet("background-color : green")
            self.statusbar.showMessage('Вероятность плагиата: 0.00%')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Antiplagiarism()
    ex.show()
    sys.exit(app.exec())
