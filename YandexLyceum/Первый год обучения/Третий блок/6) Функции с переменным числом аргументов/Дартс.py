scoring = {}


def score(type_hit, num=1):
    if type_hit == 'Яблочко':
        return 50
    elif type_hit == 'Зеленое кольцо':
        return 25
    elif type_hit == 'Внешнее_кольцо':
        return scoring[num][0]
    elif type_hit == 'Внутреннее_кольцо':
        return scoring[num][1]
