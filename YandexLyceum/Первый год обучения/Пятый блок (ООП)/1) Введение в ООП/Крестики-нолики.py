class TicTacToeBoard:
    def __init__(self):
        self.field = [['-'] * 3 for i in range(3)]
        self.end = False
        self.player = 0

    def new_game(self):
        self.__init__()

    def get_field(self):
        return self.field

    def check_field(self):
        main_diag_x = 0
        main_diag_y = 0
        for i in range(len(self.field)):
            count_in_col_x = 0
            count_in_col_y = 0
            if self.field[i].count('X') == 3:
                return 'X'
            elif self.field[i].count('0') == 3:
                return '0'

            if self.field[i][i] == 'X':
                main_diag_x += 1
                if main_diag_x == 3:
                    return 'X'
            elif self.field[i][i] == '0':
                main_diag_y += 1
                if main_diag_y == 3:
                    return '0'
            for j in range(len(self.field) - 1, -1, -1):
                if self.field[j][i] == 'X':
                    count_in_col_x += 1
                    if count_in_col_x == 3:
                        return 'X'
                elif self.field[j][i] == '0':
                    count_in_col_y += 1
                    if count_in_col_y == 3:
                        return '0'

        if self.field[0][2] == self.field[1][1] == self.field[2][0]:
            if self.field[0][2] == 'X':
                return 'X'
            elif self.field[0][2] == '0':
                return '0'
        draw = 0
        for g in self.field:
            if '-' not in g:
                draw += 1
        if draw == 3:
            return 'D'
        return

    def make_move(self, row, col):
        if not self.end:
            if self.field[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            else:
                if self.player % 2 == 0:
                    self.field[row - 1][col - 1] = 'X'
                else:
                    self.field[row - 1][col - 1] = '0'
                self.player += 1
            check = self.check_field()
            if check == 'X':
                self.end = True
                return 'Победил игрок X'
            elif check == '0':
                self.end = True
                return 'Победил игрок 0'
            elif check == 'D':
                self.end = True
                return 'Ничья'
            else:
                return 'Продолжаем играть'
        else:
            return 'Игра уже завершена'
