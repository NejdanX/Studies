def palindrome():
    with open('input.dat', 'rb') as file:
        text = file.read()
        return text == text[::-1]

