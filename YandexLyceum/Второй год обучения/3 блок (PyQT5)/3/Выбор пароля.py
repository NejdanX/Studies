import sys
DIGIT = '0123456789'
PC_KEYBORD_ENGLISH = [['qwertyuiop'], ['asdfghjkl'], ['zxcvbnm']]
PC_KEYBORD_RUSSIAN = [['йцукенгшщзхъ'], ['фывапролджэ'], ['ячсмитьбю']]


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


def check_password(password):
    if len(password) < 9:
        raise LengthError
    if password.lower() == password or password.upper() == password:
        raise LetterError
    is_num_ok = False
    is_alpha_ok = False
    for symbol in password:
        if symbol.isdigit():
            is_num_ok = True
        elif symbol.isalpha():
            is_alpha_ok = True
        if is_num_ok and is_alpha_ok:
            break
    if not is_num_ok or not is_alpha_ok:
        raise DigitError
    for i in range(len(PC_KEYBORD_RUSSIAN)):
        for j in range(len(PC_KEYBORD_RUSSIAN[i][0]) - 2):
            if PC_KEYBORD_RUSSIAN[i][0][j:j + 3] in password.lower():
                raise SequenceError
    for i in range(len(PC_KEYBORD_ENGLISH)):
        for j in range(len(PC_KEYBORD_ENGLISH[i][0]) - 2):
            if PC_KEYBORD_ENGLISH[i][0][j:j + 3] in password.lower():
                raise SequenceError
    if 'жэё' in password.lower():
        raise SequenceError
    with open('top-9999-words.txt', encoding='utf8') as file:
        for key_word in file.readlines():
            key_word = key_word.strip()
            if key_word in password:
                raise WordError
    return 'ok'


exceptions = {}
with open('top 10000 passwd.txt', encoding='utf8') as passwords:
    for password in passwords:
        try:
            check_password(password)
        except LengthError:
            exceptions['LengthError'] = exceptions.get('LengthError', 0) + 1
        except LetterError:
            exceptions['LetterError'] = exceptions.get('LetterError', 0) + 1
        except DigitError:
            exceptions['DigitError'] = exceptions.get('DigitError', 0) + 1
        except SequenceError:
            exceptions['SequenceError'] = exceptions.get('SequenceError', 0) + 1
        except WordError:
            exceptions['WordError'] = exceptions.get('WordError', 0) + 1
for key in sorted(exceptions.keys()):
    print(f'{key} - {exceptions[key]}')
