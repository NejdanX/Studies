words = {}
text = input().split()
for word in text:
    words[word] = words.get(word, 0) + 1
    print(words[word], end=' ')
