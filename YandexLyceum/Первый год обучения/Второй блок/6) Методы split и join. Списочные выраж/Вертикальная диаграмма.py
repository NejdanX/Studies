numbers = [int(x) for x in input().split()]
print('*' * (len(numbers) + 2))
print('*', ' ' * (len(numbers)), '*', sep='')
for i in range(max(numbers)):
    print('*', end='')
    for j in range(len(numbers)):
        if numbers[j] >= (max(numbers) - i):
            print('*', end='')
        else:
            print(' ', end='')
    print('*')