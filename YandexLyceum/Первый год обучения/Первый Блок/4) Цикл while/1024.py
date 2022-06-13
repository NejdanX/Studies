number = int(input())
power = 0
tries = 0
while 2 ** tries <= number:
    if(number % 2 == 0 or number == 1):
        if(2 ** tries == number):
            power = tries
            print(power)
            break
    tries += 1
if(power == 0 and number > 1):
    print("НЕТ")