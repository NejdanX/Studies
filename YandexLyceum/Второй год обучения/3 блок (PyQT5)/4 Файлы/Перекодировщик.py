TRANSLITERATION = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}

with open('cyrillic.txt', 'r', encoding='utf8') as file_from_read:
    with open('transliteration.txt', 'w', encoding='utf8') as file_to_write:
        for symbol in file_from_read.read():
            for_write = symbol
            if symbol.lower() in TRANSLITERATION:
                for_write = TRANSLITERATION[symbol.lower()].capitalize() if symbol.isupper() \
                    else TRANSLITERATION[symbol]
            file_to_write.write(for_write)