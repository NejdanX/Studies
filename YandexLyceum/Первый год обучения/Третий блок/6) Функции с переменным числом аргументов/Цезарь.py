def encrypt_caesar(msg, shift=3, encrypt=True):
    result = ""
    shift %= 32
    if not encrypt:
        shift = -shift
    let = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in range(len(msg)):
        if msg[i] in let:
            if ord(msg[i]) < ord('Я'):
                if (ord(msg[i]) + shift) > ord('Я'):
                    result += chr(ord('А') + (ord(msg[i]) + shift - ord('Я') - 1))
                elif (ord(msg[i]) + shift) < ord('А'):
                    result += chr(ord('Я') + (ord(msg[i]) + shift - ord('А') + 1))
                else:
                    result += chr(ord(msg[i]) + shift)
            else:
                if (ord(msg[i]) + shift) > 1103:
                    result += chr(ord('а') + (ord(msg[i]) + shift - ord('я') - 1))
                elif (ord(msg[i]) + shift) < ord('а'):
                    result += chr(ord('я') + (ord(msg[i]) + shift - ord('а') + 1))
                else:
                    result += chr(ord(msg[i]) + shift)
        else:
            result += msg[i]
    return result


def decrypt_caesar(encrypted, shift=3):
    return encrypt_caesar(encrypted, shift, encrypt=False)


enter_shift = int(input())
string = input()
print(encrypt_caesar(string, enter_shift, False))
