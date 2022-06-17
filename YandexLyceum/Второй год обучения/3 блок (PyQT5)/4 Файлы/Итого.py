with open('prices.txt', encoding='utf8') as file:
    amount = 0
    for string in file.readlines():
        name, count, price = string.split()
        amount += float(price) * int(count)
    print(f'{amount:.2f}')