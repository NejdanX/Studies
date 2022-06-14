multi = []
isYes = False
for i in range(int(input())):
    multi.append(int(input()))
number = int(input())
for i in range(len(multi)):
    for j in range(len(multi)):
        if(i != j):
            if(multi[i] * multi[j]) == number:
                isYes = True
                break
    if(isYes):
        break
if(isYes):
    print("ДА")
else:
    print("НЕТ")