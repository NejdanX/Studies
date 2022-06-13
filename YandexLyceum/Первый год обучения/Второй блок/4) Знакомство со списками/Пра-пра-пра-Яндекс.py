data = []
for i in range(int(input())):
    data.append(input())
search = input()
for i in range(len(data)):
    if(search in data[i]):
        print(data[i])