countString = int(input())
isCat = False
for i in range(countString):
    string = input()
    if('Кот' in string or 'кот' in string):
        isCat = True
        break
if(isCat):
    print("МЯУ")
else:
    print("НЕТ")