translated_text = ''


def translate(text):
    table = text.maketrans("", "", ".,!?-;:_аеёиуыоэяюАЕЁИУЫОЭЯЮ")
    text = text.translate(table)
    global translated_text
    translated_text = ' '.join(text.split())
