VALID_CHARACTERS = '0123456789+-()'


def check_phone_number(phone_number):
    phone_number = ''.join(phone_number.split())
    count_brackets = 0
    already_bracket = False
    count_dash = 0
    if phone_number[-1] == '-':
        return 'error'
    for symbol in phone_number:
        if symbol not in VALID_CHARACTERS:
            return 'error'
        if symbol == '(':
            if already_bracket:
                return 'error'
            count_brackets += 1
            already_bracket = True
        if symbol == ')':
            if not count_brackets:
                return 'error'
            count_brackets -= 1
        if symbol == '-':
            count_dash += 1
            if count_dash > 1:
                return 'error'
        else:
            count_dash = 0
    if count_brackets == 1:
        return 'error'
    if phone_number.startswith('8') or phone_number.startswith('+7'):
        if phone_number.startswith('8'):
            phone_number = '+7' + phone_number[1:]
        phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
        return phone_number if len(phone_number) == 12 else 'error'
    return 'error'


phone_number = input()
print(check_phone_number(phone_number))