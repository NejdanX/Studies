import sys

count_str = 0
for line in sys.stdin:
    if 'далек' in line.lower():
        count_str += 1
print(count_str)