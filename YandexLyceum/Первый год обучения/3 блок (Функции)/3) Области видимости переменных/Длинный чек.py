num_receipt = 0
items = []


def add_item(itemName, itemCost):
    items.append((itemName, itemCost))


def print_receipt():
    if not items:
        return
    amount = 0
    global num_receipt
    num_receipt += 1
    print(f"Чек {num_receipt}. Всего предметов: {len(items)}")
    for i in range(len(items)):
        print(items[i][0], '-', items[i][1])
        amount += int(items[i][1])
    print(f'Итого: {amount}')
    print('-----')
    items.clear()
