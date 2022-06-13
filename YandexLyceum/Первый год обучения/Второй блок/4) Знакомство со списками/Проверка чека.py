string = input()
count_products, expect_sum = int(string[:4]), int(string[4:])
list_wrond_string = []
sum_receipt = 0
for i in range(count_products):
    position = input()
    price, count_commodity, product = int(position[:7]), int(position[8:12]), int(position[13:])
    sum_receipt += price * count_commodity
    if(price * count_commodity != product):
        list_wrond_string.append(i + 1)
print(expect_sum - sum_receipt)
for i in range(len(list_wrond_string)):
    print(list_wrond_string[i], '', end='')