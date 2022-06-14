first = int(input())
second = int(input())
third = int(input())
if(first > second and first > third):
    if(second > third):
        print(first)
        print(second)
        print(third)
    else:
        print(first)
        print(third)
        print(second)
elif(second > first and second > third):
    if(first > third):
        print(second)
        print(first)
        print(third)
    else:
        print(second)
        print(third)
        print(first)
elif(third > first and third > second):
    if(first > second):
        print(third)
        print(first)
        print(second)
    else:
        print(third)
        print(second)
        print(first)
else:
    print(first)
    print(second)
    print(third)    