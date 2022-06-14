count_title = int(input())
result = []
for i in range(count_title):
    titles = []
    while True:
        string = input()
        if(string == '*'):
            break
        titles.extend(string.split())
    result.append('-'.join(titles))
print(', '.join(result[::-1]))