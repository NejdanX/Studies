import sys


file_name = [item for item in sys.argv[1:] if 'txt' in item]
try:
    with open(file_name[0], 'r', encoding='utf-8') as file:
        data = list(map(str.strip, file.readlines()))
        print_number = '--num' in sys.argv[1:]
        if '--sort' in sys.argv[1:]:
            data.sort()
        for index, item in enumerate(data):
            if print_number:
                print(index, end=' ')
            print(item)
        if '--count' in sys.argv[1:]:
            print('rows count:', len(data))
except FileExistsError:
    print('ERROR')
except FileNotFoundError:
    print('ERROR')
except IndexError:
    print('ERROR')