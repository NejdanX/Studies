count_str = int(input())
quotes = 0
space = 0
j = 0
for i in range(count_str):
    string = input()    
    k = 0
    j = 0
    result = ''
    if(string[0] == ' '):
        while string[j] == ' ':
            j += 1
        result += (' ' * j)
        k += j
    while k < len(string):
        if(string[k] == ' ' and quotes % 2 == 0):
            space += 1
            if(space > 1):
                j = k
                while string[j] == ' ':
                    j += 1
                space = 0
                k += (j - k) - 1
            else:
                result += ' '
        elif(string[k] == '\''):
            if(string[k - 1] != '\\' or string[k - 2:k] == '\\\\'):
                quotes += 1
            result += string[k]
        elif(string[k] == '#' and quotes % 2 == 0):
            break
        else:
            result += string[k]
            space = 0
        k += 1
    print(result)        