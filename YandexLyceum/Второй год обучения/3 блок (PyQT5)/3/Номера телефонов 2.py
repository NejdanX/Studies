VALID_CHARACTERS = '0123456789+-()'


class PhoneError(Exception):
    pass


class FormatError(PhoneError):
    pass


class NotValidSymbolError(FormatError):
    pass


class LengthError(PhoneError):
    pass


try:
    phone_number = ''.join(input().split())
    if not phone_number.startswith('8') and not phone_number.startswith('+7'):
        raise FormatError('неверный формат')
    if phone_number[-1] == '-':
        raise FormatError('неверный формат')
    if phone_number.count('(') > 1 or phone_number.count(')') > 1 or \
            phone_number.find('(') > phone_number.find(')') or \
            phone_number.count('(') != phone_number.count(')'):
        raise FormatError('неверный формат')
    if '--' in phone_number:
        raise FormatError('неверный формат')
    if phone_number.startswith('8'):
        phone_number = '+7' + phone_number[1:]
    phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
    if not all(map(lambda s: s in VALID_CHARACTERS, phone_number)):
        raise NotValidSymbolError('неверный формат')
    if len(phone_number) != 12:
        raise LengthError('неверное количество цифр')
    print(phone_number)
except FormatError as err:
    print(err)
except LengthError as err:
    print(err)

