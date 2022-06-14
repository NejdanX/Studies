count_glass = int(input())
list_position = []
on_table = 0
for i in range(1, count_glass + 1):
    string = input()
    list_position.append((i, string))
for i in range(int(input())):
    on_table = int(input())
    index = 0
    for j in range(on_table):
        number = int(input())
        for k in range(len(list_position)):
            if(list_position[k][0] == number):
                index = k
                break
        list_position[index], list_position[j] = list_position[j], list_position[index]
    for j in range(len(list_position)):
        number, string = list_position[j]
        list_position[j] = (j + 1, string)
for i in range(on_table):
    number, string = list_position[i]
    print(string)