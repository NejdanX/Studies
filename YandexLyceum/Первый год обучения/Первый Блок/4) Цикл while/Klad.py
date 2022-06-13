try:
    xK = int(input())
    yK = int(input())
    x = 0
    y = 0
    rule = input()
    direction = 0
    countCommand = 0
    minCountCommand = 0
    minDirection = 0
    flag = True
    while rule != "стоп" or rule != ' ':
        countSteps = 0
        direction = abs(direction)
        if(x == xK and y == yK and flag):
            minCountCommand = countCommand
            minDirection = direction
            flag = False
        if(rule == "вперёд"):
            countCommand += 1
            countSteps = int(input())
            if(direction >= 360):
                direction = direction - 360   
            if(direction == 0):
                y += countSteps
            elif(direction == 90):
                x += countSteps
            elif(direction == 180):
                y -= countSteps
            elif(direction == 270):
                x -= countSteps
        elif(rule == "направо"):
            countCommand += 1
            direction += 90
        elif(rule == "налево"):
            countCommand += 1
            direction -= 90
            if(direction < 0):
                direction = 360 + direction
        elif(rule == "разворот"):
            countCommand += 1
            direction -= 180
            if(direction < 0):
                direction = 360 + direction
        rule = input()
    if(minCountCommand == 0):
        minCountCommand = countCommand
        minDirection = direction
    print(minCountCommand)
    if(minDirection == 0 or minDirection == 360):
        print("север")
    elif(minDirection == 90):
        print("восток")
    elif(minDirection == 180):
        print("юг")
    elif(minDirection == 270):
        print("запад")
except EOFError:
    if(minCountCommand == 0):
        minCountCommand = countCommand
        minDirection = direction
    print(minCountCommand)
    if(minDirection == 0 or minDirection == 360):
        print("север")
    elif(minDirection == 90):
        print("восток")
    elif(minDirection == 180):
        print("юг")
    elif(minDirection == 270):
        print("запад")