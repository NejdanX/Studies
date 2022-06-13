city = set()
count_city = int(input())
for i in range(count_city):
    city.add(input())
if(input() in city):
    print("TRY ANOTHER")
else:
    print("OK")