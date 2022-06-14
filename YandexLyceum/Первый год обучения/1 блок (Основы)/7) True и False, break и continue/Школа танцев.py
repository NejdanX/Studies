patience = int(input())
rightTacts = 0
i = 0
while i != 5:
    i += 1
    rhythm = input()
    if(i == 1 and rhythm == "раз"):
        rightTacts += 1
        continue
    elif(i == 2 and rhythm == "два"):
        rightTacts += 1
        continue
    elif(i == 3 and rhythm == "три"):
        rightTacts += 1
        continue
    elif(i == 4 and rhythm == "четыре"):
        rightTacts += 1
        i = 0
        continue
    else:
        i = 0
        if(patience > 0):
            print("Правильных отсчётов было ", rightTacts, ", но теперь вы ошиблись.", sep='')
            patience -= 1
            rightTacts = 0
        if(patience == 0):
            print("На сегодня хватит.")
            patience -= 1