from random import choices, choice, shuffle


big_symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
small_symbols = 'abcdefghijkmnpqrstuvwxyz'
digits = '23456789'
ALPHABET = big_symbols + small_symbols + digits


def generate_password(m):
    password = [choice(big_symbols)] + [choice(small_symbols)] + [choice(digits)]
    shuffle(password)
    password = ''.join(password)
    password += ''.join(choices(ALPHABET, k=m - 3))
    return password


def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a
