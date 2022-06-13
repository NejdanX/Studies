def swap(first, second):
    temp = first.copy()
    first.clear()
    first += second
    second.clear()
    second += temp
