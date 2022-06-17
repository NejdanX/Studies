with open('data.txt', 'rb') as file:
    print(' ' * 10, end='')
    for i in range(16):
        if i > 9:
            print(f'0{chr(ord("a") + i - 10)}', end=' ')
        else:
            print(f'0{i}', end=' ')
    print('\n')
    new_line = 1
    string = ''
    print('000000', end='    ')
    number_of_string = hex(16)
    for dec in file.read():
        print(hex(dec)[2:].rjust(2, '0'), end=' ')
        string += chr(dec) if chr(dec).isprintable() else '.'
        if new_line % 16 == 0:
            print(' ' * 4 + string)
            print(number_of_string[2:].rjust(6, '0'), end='    ')
            number_of_string = hex(int(number_of_string, 16) + 16)
            string = ''
        new_line += 1
if new_line % 16 != 1:
    print(' ' * (48 - (new_line - 1) % 16 * 3) + ' ' * 4 + string)