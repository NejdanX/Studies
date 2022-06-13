amount = 0
price = float(input())
while price > 0:
    if(price > 1000):
        price -= price * 5 / 100
    amount += price
    price = float(input())
print(amount)