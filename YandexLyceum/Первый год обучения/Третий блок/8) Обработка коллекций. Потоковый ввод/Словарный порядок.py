words = input().split()
print(*sorted(words, key=str.lower))