import datetime as dt


system_date = dt.datetime.now()
dn = dt.timedelta(days=int(input()))
print((system_date + dn).day, (system_date + dn).month)
