import datetime as dt
from math import sin, pi

day, month, year = input().split('.')
date_born = dt.date(int(year), int(month), int(day))

day, month, year = input().split('.')
date_request = dt.date(int(year), int(month), int(day))
dd = date_request - date_born
count_day = str(dd).split()[0]
delta_time1 = dt.timedelta(days=int(count_day))
i = 0
while i != 15:
    period = 23 + i
    res = sin((2 * pi * delta_time1.days) / period) * 100
    print(round(res, 2))
    i += 5