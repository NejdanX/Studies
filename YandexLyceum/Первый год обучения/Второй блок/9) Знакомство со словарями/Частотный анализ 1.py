text = {}
marks = ['.', ',', '!', '?', ':', ';']
words = []
for _ in range(int(input())):
    string = input()
    for i in range(len(marks)):
        string = string.replace(marks[i], '')
    words += string.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()
    text[words[i]] = text.get(words[i], 0) + 1
words = list(text.items())
words.sort(key=lambda x: (-x[1], x[0]))
for word in words:
    print(word[0])