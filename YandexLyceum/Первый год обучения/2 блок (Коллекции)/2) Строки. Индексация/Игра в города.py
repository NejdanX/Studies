first = input()
second = input()
while True:
    if(second[0] != first[-1]):
        print(second)
        break
    first = second
    second = input()