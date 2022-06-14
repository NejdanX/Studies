text = {'Пяточок': ['Он украл', 'Пидор!'],
        'Хео': ['Как дела?', 'Хехе бой']}
words = list((text.items()))
words.sort(key=lambda x: x[0])
words.reverse()
for word in words:
    res = '; '.join(word[1][::-1])
    print(f'{word[0]} ~ {res}')