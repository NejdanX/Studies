numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
numbers = sorted(numbers, reverse=True)
for item in numbers:
    print(item)