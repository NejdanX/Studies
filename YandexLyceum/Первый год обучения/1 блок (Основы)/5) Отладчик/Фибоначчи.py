enteredNumber = int(input())
pre = 0
current = 1
following = 1
while True:
    print(following)
    following = pre + current
    pre = current
    current = following
    if(following > enteredNumber):
        break
    
