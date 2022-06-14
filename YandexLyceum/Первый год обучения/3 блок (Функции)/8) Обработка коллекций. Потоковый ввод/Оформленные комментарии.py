import sys


def after_sharp(string, index):
    return string[index + 1:].strip()


def main():
    strings = list(map(str.strip, sys.stdin))
    line_number = 0
    for item in strings:
        line_number += 1
        if item.find('#') != -1:
            print(f'Line {line_number}: {after_sharp(item, item.find("#"))}')
        continue


main()