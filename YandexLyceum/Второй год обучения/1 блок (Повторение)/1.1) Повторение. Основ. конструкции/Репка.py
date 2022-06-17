characters = [value for value in input().split(' -> ')]
recognise = [input() for _ in range(int(input()))]
for person in recognise:
    index_person = characters.index(person)
    if index_person == 0:
        print(f'{person} -> {characters[index_person + 1]}')
    elif index_person == len(characters) - 1:
        print(f'{characters[index_person - 1]} -> {person}')
    else:
        print(f'{characters[index_person - 1]} -> {person} -> {characters[index_person + 1]}')