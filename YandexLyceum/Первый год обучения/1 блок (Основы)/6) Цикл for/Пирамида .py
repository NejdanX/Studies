h = int(input())
rowStar = 1
countSpace = h - 1
for i in range(h):
    for j in range(countSpace):
        print(" ", end='')
    print("*" * rowStar)
    rowStar += 2
    countSpace -= 1
    