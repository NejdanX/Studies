result = ""
count_str = int(input())
for i in range(count_str):
    string = input()
    if(string[:2] == "%%"):
        print(string[2:])
    elif(string[:4] == "####"):
        continue
    else:
        print(string)