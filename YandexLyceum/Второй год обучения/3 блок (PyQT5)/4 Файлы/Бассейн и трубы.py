with open('pipes.txt', encoding='utf8') as file:
    lines = file.readlines()
    performance = list(map(float, [elem for elem in lines[:-2]]))
    working_pipes = list(map(lambda x: int(x) - 1, lines[-1].split()))
    amount = 0
    for number in working_pipes:
        amount += (1 / performance[number])
    with open('time.txt', 'w', encoding='utf8') as w_file:
        w_file.write(str(1 / amount * 60))

