word = input()
number_letter = int(input())
if number_letter > len(word) or number_letter <= 0:
    print("ОШИБКА")
else:
    print(word[number_letter - 1])