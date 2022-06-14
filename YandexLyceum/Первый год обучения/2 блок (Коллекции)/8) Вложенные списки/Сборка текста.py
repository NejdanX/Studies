order = [int(item) for item in input().split()]
sentence = input().lower().split()
for i in range(len(order)):
    if i == 0:
        print(sentence[order[i] - 1].capitalize(), end=' ')
    else:
        print(sentence[order[i] - 1], end=' ')