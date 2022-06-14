height = input()
max = 0
min = 190
count = 0
while height != "!":
    height = int(height)
    if(height >= 150 and height <= 190):
        count += 1
        if(height > max):
            max = height
        if(height < min):
            min = height
    height = input()
print(count)
print(min, max)