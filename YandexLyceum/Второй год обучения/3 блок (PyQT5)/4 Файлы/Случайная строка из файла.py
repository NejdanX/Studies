from random import choice

with open('lines.txt', 'r', encoding='utf8') as f:
    ls = f.readlines()
    if ls:
        print(choice(ls))
