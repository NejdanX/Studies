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

    def delete_row(self, row):
        self.row -= 1
        del self.table[row]

    def delete_col(self, col):
        self.col -= 1
        for i in range(len(self.table)):
            del self.table[i][col]

    def add_row(self, row):
        rest = self.table[row:]
        del self.table[row:]
        self.table.append(([0] * self.n_cols()))
        self.table += rest
        self.row += 1

    def add_col(self, col):
        for i in range(self.n_rows()):
            self.table[i].insert(col, 0)
        self.col += 1


tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()