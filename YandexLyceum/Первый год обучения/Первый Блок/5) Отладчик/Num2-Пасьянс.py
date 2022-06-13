firstHeat = int(input())
secondHeat = int(input())
while (firstHeat + secondHeat) != 0:
    heatNumber = int(input())
    take = int(input())
    if(heatNumber == 1):
        firstHeat -= take
    else:
        secondHeat -= take
    print(firstHeat, secondHeat)