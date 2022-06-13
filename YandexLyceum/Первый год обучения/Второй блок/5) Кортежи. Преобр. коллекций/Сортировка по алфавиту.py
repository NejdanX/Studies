count_string = int(input())
strings = []
for i in range(count_string):
    strings.append(input())
for i in range(len(strings) - 1):
    for j in range(len(strings) - 1 - i):
        if strings[j] > strings[j +1]:
            strings[j], strings[j + 1] = strings[j + 1], strings[j]
for i in range(len(strings)):
    print(strings[i])