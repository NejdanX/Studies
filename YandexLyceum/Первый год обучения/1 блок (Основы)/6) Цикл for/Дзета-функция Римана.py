n = int(input())
pi = 3.141592653589793
summ = 0
for i in range(1, n + 1):
    summ += (1 / i ** 2)
print((pi ** 2) / summ)