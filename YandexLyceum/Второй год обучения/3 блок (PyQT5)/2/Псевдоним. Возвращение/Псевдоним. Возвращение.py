from Psevdonim import Ui_MainWindow
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class Pseudonym(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Pseudonym, self).__init__()
        self.setupUi(self)
        self.btn_set_count.clicked.connect(self.set_count_stones)
        self.btn_take_stones.clicked.connect(self.take_stones)
        self.win_AI = True

    def set_count_stones(self):
        self.remnant_of_stones.display(self.input_count.text())
        self.moves_sheet.clear()
        self.winner.setText('')
        self.btn_take_stones.setEnabled(True)

    def take_stones(self):
        if int(self.count_take.text()) > 3 or int(self.count_take.text()) < 1:
            self.moves_sheet.addItem(f'Неверный ход: Вы пытаетесь взять неразрешенное количество камней')
            return
        elif int(self.count_take.text()) > self.remnant_of_stones.value():
            self.moves_sheet.addItem('Неверный ход: Вы пытаетесь взять больше, чем есть в куче')
            return
        self.remnant_of_stones.display(self.remnant_of_stones.value() - int(self.count_take.text()))
        self.moves_sheet.addItem(f'Игрок взял {self.count_take.text()}')
        if self.remnant_of_stones.value() == 0:
            self.won('Игрок победил!')
            return
        self.move_AI()
        if self.remnant_of_stones.value() == 0:
            self.won('ИИ победил!')

    def move_AI(self):
        AI_take = int(self.remnant_of_stones.value() % 4)
        AI_take = AI_take if AI_take else 2
        self.moves_sheet.addItem(f'ИИ взял {AI_take}')
        self.remnant_of_stones.display(self.remnant_of_stones.value() - AI_take)

    def won(self, text):
        self.winner.setText(text)
        self.btn_take_stones.setEnabled(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())