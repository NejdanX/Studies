field = [0] * 30000
commands = input()
position = 0
for i in range(len(commands)):
    if(commands[i] == '+'):
        field[position] = (field[position] + 1) % 256
    
    if(commands[i] == '-'):
        field[position] = (field[position] - 1) % 256
    
    if(commands[i] == '>'):
        position = (position + 1) % 30000
    
    if(commands[i] == '<'):
        position = (position - 1) % 30000
    
    if(commands[i] == '.'):
        print(field[position])