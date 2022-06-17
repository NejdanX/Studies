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
    is_not_sequence = True
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
    return 'ok'


# check_password("78rgyujlkoldmkl")
try:
    print(check_password("78rgyujlkoldmkl"))
except Exception as error:
    print(error.__class__.__name__)