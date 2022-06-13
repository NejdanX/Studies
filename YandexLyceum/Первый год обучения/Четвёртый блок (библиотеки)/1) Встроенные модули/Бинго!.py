from random import choices, sample, randint


def make_bingo():
    list_num = sample(range(1, 75), 25)
    list_num[12] = 0
    list_num = tuple(list_num)
    res = ()
    i = 0
    while i != 25:
        res += tuple((list_num[i: i + 5],))
        i += 5
    return res
