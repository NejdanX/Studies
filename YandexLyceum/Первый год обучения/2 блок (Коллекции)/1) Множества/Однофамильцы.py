man = set()
also_man = set()
count_also_surname = 0
for i in range(int(input())):
    surname = input()
    if surname in man:
        if surname in also_man:
            count_also_surname += 1
        else:
            also_man.add(surname)
            count_also_surname += 2
    man.add(surname)
print(count_also_surname)