count_classmate = int(input())
list_classmate = []
for i in range(count_classmate):
    list_classmate.append(input())
    print(list_classmate[i])
print()
for i in range(len(list_classmate)):
    if('4' in list_classmate[i] or '5' in list_classmate[i]):
        print(list_classmate[i])