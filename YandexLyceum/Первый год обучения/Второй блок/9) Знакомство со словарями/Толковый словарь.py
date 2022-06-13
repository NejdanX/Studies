dictionary = {}
for i in range(int(input())):
    string = input()
    dictionary[string[0:string.find(' ')]] = string[string.find(' ') + 1:]
for i in range(int(input())):
    print(dictionary.get(input(), 'Нет в словаре'))