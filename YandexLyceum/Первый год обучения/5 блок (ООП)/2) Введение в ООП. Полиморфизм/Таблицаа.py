from copy import copy


class Table:
    def __init__(self, row, col):
        self.row = copy(row)
        self.col = copy(col)
        self.table = [[0] * col for i in range(row)]

    def get_value(self, row, col):
        if row >= self.row or col >= self.col or col < 0 or row < 0:
            return None
        return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.row

    def n_cols(self):
        return self.col
