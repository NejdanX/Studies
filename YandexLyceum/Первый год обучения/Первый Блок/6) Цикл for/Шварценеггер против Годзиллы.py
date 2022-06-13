num, denum = 0, 1
countShot = int(input())
for i in range(countShot):
    a = int(input())
    b = int(input())
    num = num * b + a * denum
    denum *= b
x, y = num, denum
while y > 0:
    x, y = y, x % y
print(num // x, '/', denum // x, sep='')
