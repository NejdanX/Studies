string = input()
passwd = []
while string != '':
    passwd.append(string)
    string = input()
frequent_password = [x for x in input().split(';')]
for i in range(len(passwd)):
    temporal_list = passwd[i].split(':')
    if(temporal_list[1] in frequent_password):
        print("To:", temporal_list[0])
        print(temporal_list[4].split(',')[0],
              ", ваш пароль слишком простой, смените его.", sep='')