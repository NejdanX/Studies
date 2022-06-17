import sys

count_str = 0

for line in sys.stdin:
    line = line.replace('"', '').replace("'", '').replace('(', '').replace(')', '')
    if 'далек' in line.lower():
        count_str = count_str + int(len([word for word in line.split() if word.lower()[:5] == 'далек']) > 0)
print(count_str)