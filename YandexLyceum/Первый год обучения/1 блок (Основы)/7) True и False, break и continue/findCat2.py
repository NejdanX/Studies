catHere = -1
stringNumber = 1
string = input()
while string != "СТОП":
    if('Кот' in string or 'кот' in string):
        catHere = stringNumber
        break
    stringNumber += 1
    string = input()
print(catHere)