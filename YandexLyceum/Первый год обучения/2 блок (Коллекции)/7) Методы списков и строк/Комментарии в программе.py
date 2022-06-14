count_string = int(input()[1:])
for i in range(count_string):
    string = input() 
    ready_string = string.split('#')
    ready_string = ready_string.rstrip()
    print(ready_string)