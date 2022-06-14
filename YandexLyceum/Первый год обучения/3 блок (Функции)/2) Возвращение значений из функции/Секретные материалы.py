def print_document(pages):
    for page in pages:
        if 'Секретно' in page:
            print('Дальнейшие материалы засекречены')
            return
        print(page)
    print('Напечатано без купюр')
