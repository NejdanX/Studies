words = {}

def main():
    for i in range(int(input())):
        words[input().lower()] = ''

    list_words = [key for key in words.keys()]
    for word in list_words:
        w = sorted(word)
        for key in words:
            if w == sorted(key) and word != key:
                words[word] += key + ' '
                del list_words[list_words.index(key)]

    for item in words.items():
        if item[1] == '':
            continue
        print(item[0], item[1].strip())



objects = [1, 2, 1, 2, 3]
print(len(set([id(i) for i in objects])))
