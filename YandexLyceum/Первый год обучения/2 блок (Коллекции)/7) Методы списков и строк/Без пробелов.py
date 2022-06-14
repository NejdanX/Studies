string = input()
count_symbols = len(string)
count_symbols -= (string.count(' ') + string.count('\t'))
print(count_symbols)