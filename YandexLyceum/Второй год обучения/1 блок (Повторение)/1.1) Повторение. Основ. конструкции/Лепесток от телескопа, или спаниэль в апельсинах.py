import sys
word = ''.join(sorted(input()))
count_word = 0
result = []
for line in sys.stdin:
    line = line.rstrip('\n')
    copy_word = word
    for c in line:
        if c not in copy_word:
            break
        copy_word = copy_word.replace(c, '', 1)
    else:
        result.append(line)
        count_word += 1


print(count_word)
print(*result, sep='\n')
