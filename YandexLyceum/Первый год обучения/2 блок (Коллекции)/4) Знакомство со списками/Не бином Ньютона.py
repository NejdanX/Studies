numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
for i in range(len(numbers) - 1):
    print(numbers[i] + numbers[i + 1])