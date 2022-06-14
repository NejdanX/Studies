def print_some_primes(criterion):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for number in filter(criterion, primes):
        print(number)


# print_some_primes(lambda x: True)
just_list = [int(input()) for i in range(5)]
print(just_list)
print(list(filter(lambda x: x > 0, just_list)))
print(list(map(lambda x: abs(x), just_list)))
