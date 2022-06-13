price = int(input())
haveBought = False
haveSold = False
while price != 0:
    previousPrice = price
    price = int(input())
    if(price > previousPrice and not haveBought):
        buyStock = price
        haveBought = True
    if(price < previousPrice and not haveSold and haveBought):
        sellStock = price
        haveSold = True
print(buyStock, sellStock, sellStock - buyStock)