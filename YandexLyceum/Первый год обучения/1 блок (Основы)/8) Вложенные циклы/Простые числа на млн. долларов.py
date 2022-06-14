prime_number = int(input())
for i in range(2, prime_number):
    isPrime = True
    for j in range(2, i // 2 + 1):
        if(i % j == 0):
            isPrime = False
            break
    if(isPrime):
        print(i)