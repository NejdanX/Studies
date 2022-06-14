birthdays = {}
for _ in range(int(input())):
    string = input()
    name = string[0:string.find(' ')]
    day = int(string[string.find(' ') + 1:string.rfind(' ')])
    month = string[string.rfind(' ') + 1:]
    if(month in birthdays):
        birthdays[month] += [(day, name)]
    else:
        birthdays[month] = [(day, name)]

for key in birthdays.keys():
    for i in range(len(birthdays[key]) - 1):
        for j in range(len(birthdays[key]) - 1 - i):
            if(birthdays[key][j] > birthdays[key][j + 1]):
                birthdays[key][j], birthdays[key][j + 1] = \
                    birthdays[key][j + 1], birthdays[key][j]
            
for _ in range(int(input())):
    month = input()
    if(month in birthdays):
        for i in range(len(birthdays[month])):
            print(birthdays[month][i][1], ' ', birthdays[month][i][0], sep='', end='')
            if(i != len(birthdays[month]) - 1):
                print(' ', end='')
        print()
    else:
        print()