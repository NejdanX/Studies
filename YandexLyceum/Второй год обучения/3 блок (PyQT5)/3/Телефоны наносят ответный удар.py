VALID_CHARACTERS = '0123456789+-()'
MTS_CODES = [i for i in range(910, 920)] + [i for i in range(980, 990)]
MEGAFON_CODES = [i for i in range(920, 940)]
BEELINE_CODES = [i for i in range(902, 907)] + [i for i in range(960, 970)]
OPERATORS_CODES = MTS_CODES + MEGAFON_CODES + BEELINE_CODES
COUNTRIES_CODES = ['359', '55', '1']


class PhoneError(Exception):
    pass


class FormatError(PhoneError):
    pass


class NotValidSymbolError(FormatError):
    pass


class LengthError(PhoneError):
    pass


class OperatorError(PhoneError):
    pass


class CountryCodeError(PhoneError):
    pass


def check_phone_number(phone_number):
    if phone_number[0] != '+' and phone_number[0] != '8':
        raise FormatError('неверный формат')
    if phone_number[-1] == '-':
        raise FormatError('неверный формат')
    if phone_number.count('(') > 1 or phone_number.count(')') > 1 or \
            phone_number.find('(') > phone_number.find(')') or \
            phone_number.count('(') != phone_number.count(')'):
        raise FormatError('неверный формат')
    if '--' in phone_number:
        raise FormatError('неверный формат')
    our_country_code = False
    for code in COUNTRIES_CODES:
        if phone_number.startswith('8'):
            our_country_code = True
            phone_number = '+7' + phone_number[1:]
            break
        if phone_number.startswith('+7'):
            our_country_code = True
            break
        if phone_number[1:].startswith(code):
            break
    else:
        raise CountryCodeError('не определяется код страны')
    phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
    if not all(map(lambda s: s in VALID_CHARACTERS, phone_number)):
        raise NotValidSymbolError('неверный формат')
    if len(phone_number) != 12:
        raise LengthError('неверное количество цифр')
    if our_country_code and int(phone_number[2:5]) not in OPERATORS_CODES:
        raise OperatorError('не определяется оператор сотовой связи')
    return phone_number


try:
    phone_number = ''.join(input().split())
    print(check_phone_number(phone_number))
except PhoneError as err:
    print(err)

