col = int(input())
row = int(input())
for i in range(1, row + 1):
    for j in range(1, col + 1):
        print(j / i, "", end='')
    print()