def quarter(x, y):
    if x > 0 and y > 0:
        return 'I'
    if x < 0 and y > 0:
        return 'II'
    if x < 0 and y < 0:
        return 'III'
    return 'IV'


count_coordinate = int(input())
dict_for_quarter = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
for i in range(count_coordinate):
    coordinate = tuple(map(int, input().split()))
    if 0 in coordinate:
        print(coordinate)
    else:
        dict_for_quarter[quarter(*coordinate)] += 1
for key, value in dict_for_quarter.items():
    if key != 'IV':
        print(f'{key}: {value}', end=', ')
    else:
        print(f'{key}: {value}.')
