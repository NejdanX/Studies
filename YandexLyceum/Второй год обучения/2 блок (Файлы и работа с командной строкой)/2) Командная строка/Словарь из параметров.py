import sys

file_name = [item for item in sys.argv[1:] if 'txt' in item]
try:
    print('NENE')
    with open(file_name[0], 'r', encoding='utf-8') as file:
        data = file.readlines()
        print_number = '--num' in sys.argv[1:]
        print(data)
        if '--sort' in sys.argv[1:]:
            data.sort()
        for index, item in enumerate(data):
            print(index, item if print_number else item)
        if '--count' in sys.argv[1:]:
            print(len(sys.argv[1:]))
except FileExistsError:
    print('ERROR')
except FileNotFoundError:
    print('ERROR')
except IndexError:
    print('ERROR')