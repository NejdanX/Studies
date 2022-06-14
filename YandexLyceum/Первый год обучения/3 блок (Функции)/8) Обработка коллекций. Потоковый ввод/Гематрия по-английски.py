import sys

words = list(map(str.strip, sys.stdin))
words_with_gematria = []
for word in words:
    gematria = 0
    for i in range(len(word)):
        gematria += (ord(word[i].upper()) - ord('A') + 1)
    words_with_gematria.append((gematria, word))

words_with_gematria.sort()
for word in words_with_gematria:
    print(word[1])
