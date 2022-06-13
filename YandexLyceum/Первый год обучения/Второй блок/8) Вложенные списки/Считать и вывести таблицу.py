row = int(input())
col = int(input())
table = [[0] * col for i in range(row)]
for i in range(row):
    for j in range(col):
        table[i][j] = input()

for i in range(row):
    for j in range(col):
        print(table[i][j], end='\t')
    print()