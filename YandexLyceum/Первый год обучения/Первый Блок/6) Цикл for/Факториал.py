n = int(input())
if(n == 0):
    n = 1
for i in range(n - 1, 0, -1):
    n *= i
print(n)