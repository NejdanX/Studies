count_cycle = int(input())
sum_higs = 0
alarm = False
for i in range(1, count_cycle + 1):
    count_particle = 0
    count_W = 0
    count_Z = 0
    count_b = 0
    count_t = 0
    particle = input()
    
    while particle != "КОНЕЦ ЭКСПЕРИМЕНТА":
        if(alarm):
            count_particle -= 1
            alarm = False
            particle = ""
            continue
        else:
            if('W' in particle):
                count_W += 1
            if('Z' in particle):
                count_Z += 1
            if('b' in particle):
                count_b += 1
            if('t' in particle):
                count_t += 1
            if(particle == "ALARM!"):
                alarm = True
            else:
                count_particle += 1
        particle = input()
    higs = (count_W // 2) + (count_Z // 2) + (count_b // 2) + (count_t // 2)
    sum_higs += higs
    print(i, count_particle, higs)
print("Всего бозонов Хиггса:", sum_higs)