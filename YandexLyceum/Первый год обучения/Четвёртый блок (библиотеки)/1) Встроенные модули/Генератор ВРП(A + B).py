from random import choice, sample, shuffle


big_symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
small_symbols = 'abcdefghijkmnpqrstuvwxyz'
digits = '23456789'
ALPHABET = big_symbols + small_symbols + digits


def generate_password(m):
    password = set([choice(big_symbols)] + [choice(small_symbols)] + [choice(digits)])
    while len(password) < m:
        password = password.union(set(choice(ALPHABET)))
    password = list(password)
    shuffle(password)
    return ''.join(password)


def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 56), sep="\n")