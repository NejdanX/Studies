countCommand = int(input())
isWarWithOstasia = False
for i in range(countCommand):
    command = input()
    if(command == "С кем война?"):
        if(isWarWithOstasia):
            print("Остазия")
        else:
            print("Евразия")
    elif(command == "С кем мир?"):
        if(not isWarWithOstasia):
            print("Остазия")
        else:
            print("Евразия")
    else:
        if(isWarWithOstasia):
            isWarWithOstasia = False
        else:
            isWarWithOstasia = True