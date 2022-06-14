a = int(input())
b = int(input())
symbol = input()
for i in range(a):
    for j in range(b):
        if i == 0 or i == (a - 1):
            print(symbol, end='')
        elif j == 0 or j == (b - 1):
            print(symbol, end='')
        else:
            print(" ", end='')
    print()