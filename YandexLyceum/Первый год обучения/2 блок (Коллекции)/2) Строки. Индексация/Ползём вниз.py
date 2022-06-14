move = input() + ' '
print(move[0], end='')
count_space = 0
for i in range(1, len(move)):
    if(move[i] == 'V' and move[i + 1] != '<'):
        print('\n', count_space * ' ', move[0], sep='', end='')
    if(move[i] == '>'):
        print(move[0], end='')
        count_space += 1
    if(move[i] == 'V' and move[i + 1] == '<'):
        print()
        left = 0
        j = i + 1
        while True:
            if(move[j] == '<'):
                left += 1
            else:
                break
            j += 1
        i += left
        count_space -= left
        print(count_space * ' ', move[0], sep='', end='')
        for k in range(left):
            print(move[0], end='')