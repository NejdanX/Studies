DIGIT = '0123456789'
PC_KEYBORD_ENGLISH = [['qwertyuiop'], ['asdfghjkl'], ['zxcvbnm']]
PC_KEYBORD_RUSSIAN = [['йцукенгшщзхъ'], ['фывапролджэ'], ['ячсмитьбю']]


def check_password(password):
    assert len(password) > 8
    assert password.lower() != password and password.upper() != password
    is_num_ok = False
    is_alpha_ok = False
    for symbol in password:
        if symbol.isdigit():
            is_num_ok = True
        elif symbol.isalpha():
            is_alpha_ok = True
        if is_num_ok and is_alpha_ok:
            break
    assert is_num_ok and is_alpha_ok
    for i in range(len(PC_KEYBORD_RUSSIAN)):
        for j in range(len(PC_KEYBORD_RUSSIAN[i][0]) - 2):
            assert PC_KEYBORD_RUSSIAN[i][0][j:j + 3] not in password.lower()
    for i in range(len(PC_KEYBORD_ENGLISH)):
        for j in range(len(PC_KEYBORD_ENGLISH[i][0]) - 2):
            assert PC_KEYBORD_ENGLISH[i][0][j:j + 3] not in password.lower()
    assert 'жэё' not in password.lower()
    return 'ok'


try:
    password = input()
    print(check_password(password))
except AssertionError:
    print('error')
except Exception as err:
    print('error')