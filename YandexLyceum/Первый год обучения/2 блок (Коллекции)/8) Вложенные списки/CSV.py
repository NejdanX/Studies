row = int(input())
table = [[el for el in input().split(',')] for i in range(row)]
for i in range(int(input())):
    r, c = input().split(',')
    r, c = int(r), int(c)
    print(table[r][c])
