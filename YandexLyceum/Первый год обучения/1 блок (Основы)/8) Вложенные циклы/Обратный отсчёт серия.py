countStarter = int(input())
start = 0
for i in range(1, countStarter + 1):
    for j in range(start, -1, -1):
        print("Осталось секунд:", j)
    print("Пуск", i)
    start += 1