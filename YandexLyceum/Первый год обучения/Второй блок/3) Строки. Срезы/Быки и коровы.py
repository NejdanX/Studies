first = input()
second = input()
cow = 0
bull = 0
for i in range(len(first)):
    if(first[i] == second[i]):
        bull += 1
    elif(first[i] in second):
        cow += 1
print(bull, cow)