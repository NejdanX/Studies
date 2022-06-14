count_string = int(input())
length_strings = []
for i in range(count_string):
    string = input()
    length_strings.append((string, len(string)))
for i in range(len(length_strings) - 1):
    for j in range(len(length_strings) - 1 - i):
        word, length = length_strings[j]
        word2, length2 = length_strings[j + 1]
        if length > length2:
            length_strings[j], length_strings[j + 1] = length_strings[j + 1], length_strings[j]
        elif length == length2:
            if word > word2:
                length_strings[j], length_strings[j + 1] = length_strings[j + 1], length_strings[j]
for i in range(len(length_strings)):
    string, number = length_strings[i]
    print(string)