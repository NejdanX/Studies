stack = input().split(' ')
i = 0
while len(stack) != 1:
    if(stack[i] == '-'):
        del stack[i]
        stack.insert(i - 2, int(stack.pop(i - 2)) - int(stack.pop(i - 2)))
        i = 0
    elif(stack[i] == '+'):
        del stack[i]
        stack.insert(i - 2, int(stack.pop(i - 2)) + int(stack.pop(i - 2)))
        i = 0 
    elif(stack[i] == '*'):
        del stack[i]
        stack.insert(i - 2, int(stack.pop(i - 2)) * int(stack.pop(i - 2)))
        i = 0         
    i += 1
print(str(stack[0]))