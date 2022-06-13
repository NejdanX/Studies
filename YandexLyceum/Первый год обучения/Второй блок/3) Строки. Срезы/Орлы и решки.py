string = input()
max_eagle = 0
count_eagle = 0
for i in range(len(string)):
    if(string[i] == 'о'):
        count_eagle += 1
        if(max_eagle < count_eagle):
            max_eagle = count_eagle        
    if(string[i] == 'р'):
        count_eagle = 0
print(max_eagle)