catHere = -1
stringNumber = 1
countCat = 0
string = input()
while string != "СТОП":
    if('Кот' in string or 'кот' in string):
        if(catHere == -1):
            catHere = stringNumber
        countCat += 1
    stringNumber += 1
    string = input()
print(countCat, catHere)