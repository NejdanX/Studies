count_string = 0
while True:
    string = input()
    if('сам' in string and 'лучш' in string):
        count_string += 1
    else:
        break
print(count_string)