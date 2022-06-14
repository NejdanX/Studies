daily_food = [0, 150, 150]


def count_food(days):
    amount = 0
    for index in days:
        amount += daily_food[index - 1]
    return amount
