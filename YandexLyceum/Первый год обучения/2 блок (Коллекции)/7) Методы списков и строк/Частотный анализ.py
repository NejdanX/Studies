d = input()
string = d.replace(' ', '')
string = "".join(sorted(string.lower()))
list_inputs = []
maximum = 0
char = ''
while string:
    index = string.rfind(string[0])
    if (index + 1) > maximum:
        maximum = index + 1
        char = string[0]
    if (index + 1) == maximum:
        if(char > string[0]):
            char = string[0]
    string = string[index + 1:]
print(char)