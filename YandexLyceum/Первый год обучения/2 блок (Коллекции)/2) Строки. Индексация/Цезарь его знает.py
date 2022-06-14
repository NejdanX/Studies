shift = int(input()) % 32
string = input()
result = ""
let = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(string)):
    if string[i] in let:
        if ord(string[i]) <= ord('Я'):
            if(ord(string[i]) + shift) > ord('Я'):
                result += chr(ord('А') + (ord(string[i]) + shift - ord('я') - 1))
            else:
                result += chr(ord(string[i]) + shift)            
        else:
            if(ord(string[i]) + shift) > 1103:
                result += chr(ord('а') + (ord(string[i]) + shift - ord('я') - 1))
            else:
                result += chr(ord(string[i]) + shift)
    else:
        result += string[i]
print(result)