number = int(input())
count = 0
for i in range(1, number + 1):
    if(number % i == 0):
        if(i != number):
            print(i, "", end='')
        else:
            print(i, sep='')
        count += 1
if(count == 2):
    print("ПРОСТОЕ")
else:
    print("НЕТ")
    