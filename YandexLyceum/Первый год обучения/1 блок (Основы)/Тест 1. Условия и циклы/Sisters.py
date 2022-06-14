elsi = float(input())
Leisi = float(input())
Tilli = float(input())
time = int(input())
water = int(input())
somebodyCan = False
if(elsi * (time * 60) >= water):
    print("Элси", end='')
    somebodyCan = True
if(Leisi * (time * 60) >= water):
    if(somebodyCan):
        print(" Лейси", end='')
    else:
        print("Лейси", end='')
    somebodyCan = True
if(Tilli * (time * 60) >= water):
    if(somebodyCan):
        print(" Тилли", end='')
    else:
        print("Тилли", end='')
    somebodyCan = True
if(not somebodyCan):
    print("Не могут")
