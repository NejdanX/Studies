def from_chess(cell):
    a = cell[0]
    b = int(cell[1])
    a = 'ABCDEFGH'.find(a) + 1
    return (a, b)


def in_chess(cell):
    (a, b) = cell
    return 'ABCDEFGH'[a - 1] + str(b)


def possible_turns(cell):
    row, col = from_chess(cell)
    steps = []
    for _ in range(8):
        steps.append((row + 2, col + 1))
        steps.append((row + 2, col - 1))
        steps.append((row - 2, col + 1))
        steps.append((row - 2, col - 1))
        steps.append((row + 1, col + 2))
        steps.append((row + 1, col - 2))
        steps.append((row - 1, col + 2))
        steps.append((row - 1, col - 2))
    res = []
    for i in range(8):
        a, b = steps[i][0], steps[i][1]
        if 0 < a < 9 and 0 < b < 9:
            res.append(in_chess((a, b)))
    return sorted(res)
