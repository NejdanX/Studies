# Блок - случаной число, служебные данные, хэш данного блока и хэш предыдущего блока
# bn включает полезную информацию mn, представленную нат. числом, rn - случайное число
# от 0 до 255. hn - хэш(целое число от 0 до 255). hn = 37*(mn + rn + hn-1) % 256. h0 = 0
# bn - одно число. Требуется, чтобы hn < 100. bn = hn + rn*256 + mn*256^2
countBlock = int(input())
wrongBlockchainNumber = -1
h = 0
for i in range(countBlock):
    previousHash = h
    b = int(input())
    h = b % 256
    b //= 256
    r = b % 256
    b //= 256
    m = b
    if((h != 37 * (m + r + previousHash) % 256) or (h >= 100)) and wrongBlockchainNumber == -1:
        wrongBlockchainNumber = i
print(wrongBlockchainNumber)