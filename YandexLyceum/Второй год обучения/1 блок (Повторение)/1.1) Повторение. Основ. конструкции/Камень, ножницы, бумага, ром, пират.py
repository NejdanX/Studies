def winner(first, second):
    if first == second:
        return 'ничья'
    if (first == 'бумага' and (second == 'камень' or second == 'пират')) or \
            (first == 'камень' and (second == 'ножницы' or second == 'ром')) or \
            (first == 'ножницы' and (second == 'бумага' or second == 'ром')) or \
            (first == 'пират' and (second == 'ножницы' or second == 'камень')) or \
            (first == 'ром' and (second == 'бумага' or second == 'пират')):
        return 'первый'
    return 'второй'


choice_first_pirate = input()
choice_second_pirate = input()
print(winner(choice_first_pirate, choice_second_pirate))