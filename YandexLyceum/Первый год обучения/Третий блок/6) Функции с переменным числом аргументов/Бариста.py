ingredients = []
drinks = {'Эспрессо': [1, 0, 0],
          'Капучино': [1, 3, 0],
          'Маккиато': [2, 1, 0],
          'Кофе по-венски': [1, 0, 2],
          'Латте Маккиато': [1, 2, 1],
          'Кон Панна': [1, 0, 1]
          }


def choose_coffee(*args):
    for i in range(len(args)):
        drink = args[i]
        rest_corn = ingredients[0] - drinks[drink][0]
        rest_milk = ingredients[1] - drinks[drink][1]
        rest_cream = ingredients[2] - drinks[drink][2]
        if rest_corn < 0 or rest_milk < 0 or rest_cream < 0:
            continue
        ingredients[0] -= drinks[drink][0]
        ingredients[1] -= drinks[drink][1]
        ingredients[2] -= drinks[drink][2]
        return drink
    return "К сожалению, не можем предложить Вам напиток."


ingredients = [0, 0, 0]
print(choose_coffee("Кофе по-венски"))