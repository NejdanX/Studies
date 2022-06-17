def winner(first, second):
    if first == second:
        return 'ничья'
    if (first == 'бумага' and second == 'камень') or (first == 'камень' and second == 'ножницы') or \
            (first == 'ножницы' and second == 'бумага'):
        return 'первый'
    return 'второй'


choice_first_pirate = input()
choice_second_pirate = input()
print(winner(choice_first_pirate, choice_second_pirate))
