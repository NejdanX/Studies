class SeaMap:
    def __init__(self):
        self.field = [['.'] * 10 for i in range(10)]


    def shoot(self, row, col, result):
        if result == 'miss':
            self.field[row][col] = '*'
        elif result == 'hit':
            self.field[row][col] = 'x'
        else:
            self.field[row][col] = 'x'
            self.check(row, col)

    def cell(self, row, col):
        return self.field[row][col]

    def check(self, row, col):
        if row == 0 and col == 0:
            pass



sm = SeaMap()
sm.shoot(0, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')
sm.shoot(9, 9, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()