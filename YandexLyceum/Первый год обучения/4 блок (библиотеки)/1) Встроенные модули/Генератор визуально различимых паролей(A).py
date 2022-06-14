from random import sample
from string import ascii_letters, digits


symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
ALPHABET = ascii_letters.replace('I', '').replace('l', '').replace('O', '').replace('o', '') \
           + digits.replace('1', '').replace('0', '')


def generate_password(m):
    return ''.join(sample(ALPHABET, k=m))


def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a


print(*main(5, 10), sep='\n')