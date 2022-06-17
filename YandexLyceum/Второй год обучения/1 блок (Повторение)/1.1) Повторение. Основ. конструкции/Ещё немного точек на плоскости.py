count_coordinate = int(input())
coordinate = tuple(map(int, input().split()))
dict_for_outside = {'left': coordinate, 'right': coordinate, 'top': coordinate, 'bottom': coordinate}
for i in range(count_coordinate):
    if i != 0:
        coordinate = tuple(map(int, input().split()))
    for key, value in dict_for_outside.items():
        if coordinate[0] > value[0] and key == 'right':
            dict_for_outside[key] = coordinate
        if coordinate[0] < value[0] and key == 'left':
            dict_for_outside[key] = coordinate
        if coordinate[1] > value[1] and key == 'top':
            dict_for_outside[key] = coordinate
        if coordinate[1] < value[1] and key == 'bottom':
            dict_for_outside[key] = coordinate
    if abs(coordinate[1]) < abs(coordinate[0]):
        print(coordinate)
for key, value in dict_for_outside.items():
    print(f'{key}: {value}')