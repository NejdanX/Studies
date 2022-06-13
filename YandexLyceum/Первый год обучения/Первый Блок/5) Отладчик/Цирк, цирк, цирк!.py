heat = int(input())
countMove = 0
while heat != 1:
    if(heat % 2 == 0):
        heat /= 2
    else:
        heat -= 1
    countMove += 1
print(countMove)