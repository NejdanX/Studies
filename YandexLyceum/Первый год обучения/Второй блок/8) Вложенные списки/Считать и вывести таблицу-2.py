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
print()

for i in range(col):
    for j in range(row):
        print(table[j][i], end='\t')
    print()