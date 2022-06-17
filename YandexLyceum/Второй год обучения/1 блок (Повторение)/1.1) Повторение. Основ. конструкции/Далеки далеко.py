import sys


FIND_IT = ['далек', 'далеку', 'далека', 'далеком', 'далеке',
           'далеки', 'далеков', 'далекам', 'далеками', 'далеках']
count_str = 0
for line in sys.stdin:
    line = line.replace('"', '').replace("'", '').replace('(', '').replace(')', '')
    count_str += int(len([word for word in line.split() if word.lower() in FIND_IT]) > 0)
print(count_str)