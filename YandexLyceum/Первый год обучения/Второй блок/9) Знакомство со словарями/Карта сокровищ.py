coordinates = {}
for i in range(int(input())):
    x, y = input().split()
    key = x[:len(x) - 1] + y[:len(y) - 1]
    coordinates[key] = coordinates.get(key, 0) + 1
    
maximum = 0
for value in coordinates.values():
    if(value > maximum):
        maximum = value
print(maximum)