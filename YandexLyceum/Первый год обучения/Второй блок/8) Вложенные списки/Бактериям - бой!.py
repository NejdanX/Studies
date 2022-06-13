size = int(input())
battlefield = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(input()))
    battlefield.append(row)
count_shot = int(input())
while count_shot != 0:
    count_shot -= 1
    y = int(input())
    x = int(input())
    battlefield[x][y] -= 8
    if(x == 0 and y == 0):
        battlefield[x][y + 1] -= 4
        battlefield[x + 1][y] -= 4
        battlefield[x + 1][y + 1] -= 4
    elif(x == 0 and y == size - 1):
        battlefield[x][y - 1] -= 4
        battlefield[x + 1][y - 1] -= 4   
        battlefield[x + 1][y] -= 4     
    elif(x == size - 1 and y == 0):
        battlefield[x - 1][y] -= 4
        battlefield[x - 1][y + 1] -= 4   
        battlefield[x][y + 1] -= 4
    elif(x == size - 1 and y == size - 1):
        battlefield[x - 1][y] -= 4
        battlefield[x - 1][y - 1] -= 4   
        battlefield[x][y - 1] -= 4
    elif(x == 0 and y > 0):
        battlefield[x][y - 1] -= 4
        battlefield[x][y + 1] -= 4 
        battlefield[x + 1][y - 1] -= 4
        battlefield[x + 1][y + 1] -= 4 
        battlefield[x + 1][y] -= 4         
    elif(x > 0 and y == 0):  
        battlefield[x - 1][y] -= 4
        battlefield[x + 1][y] -= 4 
        battlefield[x - 1][y + 1] -= 4
        battlefield[x + 1][y + 1] -= 4 
        battlefield[x][y + 1] -= 4
    elif(x > 0 and y == size - 1):
        battlefield[x + 1][y] -= 4
        battlefield[x - 1][y] -= 4 
        battlefield[x + 1][y - 1] -= 4
        battlefield[x - 1][y - 1] -= 4 
        battlefield[x][y - 1] -= 4
    elif(x == size - 1 and y > 0):
        battlefield[x][y + 1] -= 4
        battlefield[x][y - 1] -= 4 
        battlefield[x - 1][y + 1] -= 4
        battlefield[x - 1][y - 1] -= 4 
        battlefield[x - 1][y] -= 4            
    else:
        x -= 1
        y -= 1
        for i in range(3):
            for j in range(3):
                if(i + x == x + 1 and j + y == y + 1):
                    continue
                battlefield[x + i][y + j] -= 4  
                
for i in range(size):
    for j in range(size):
        if(battlefield[i][j] < 0):
            battlefield[i][j] = 0
        print(battlefield[i][j], end=' ')
    print()