d = int(input())
m = int(input())
year = int(input())
if((m - 2) > 0):
    m -= 2
else:
    m = 12 - abs(m - 2)
    year -= 1
c = year // 100
y = year % 100
weekDay = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(weekDay)