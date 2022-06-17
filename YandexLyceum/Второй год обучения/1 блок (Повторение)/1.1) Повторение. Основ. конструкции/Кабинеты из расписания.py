import sys

lesson = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line.isalpha() and line:
        splited_line = line.split()
        if (int(splited_line[-1]), ' '.join(splited_line[:-1])) not in lesson:
            lesson.append((int(splited_line[-1]), ' '.join(splited_line[:-1])))
lesson = sorted(list(lesson), key=lambda x: x[0])
print(f'{lesson[0][0]}: {lesson[0][1]}', end='')
for i in range(1, len(lesson)):
    if lesson[i][0] == lesson[i - 1][0]:
        print(f', {lesson[i][1]}', end='')
    else:
        print(f'\n{lesson[i][0]}: {lesson[i][1]}', end='')