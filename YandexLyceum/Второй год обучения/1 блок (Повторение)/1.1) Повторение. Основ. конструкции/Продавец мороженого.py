ice_cream_var = {}
for i in range(int(input())):
    vary = input().split('\t')
    ice_cream_var[vary[0]] = int(vary[1])
input()
orders = [0]
while True:
    ice_cream = input()
    if ice_cream == '':
        orders.append(0)
        continue
    if ice_cream == '.':
        break
    position_value = ice_cream_var[ice_cream.split('\t')[0]] * int(ice_cream.split('\t')[1])
    orders[len(orders) - 1] += position_value
count_zero = 0
for i in range(1, len(orders) + 1):
    if orders[i - 1] != 0:
        print(f'{i - count_zero}) {orders[i - 1]}')
    else:
        count_zero += 1
        continue
print('Итого:', sum(orders))

'''3
Шоколадное в стаканчике	50
Эскимо на палочке	45
Сливочное	20
Шоколадное в стаканчике	5


Эскимо на палочке	1
Сливочное	2
.'''