VOWEL = ['a', 'e', 'i', 'o', 'u', 'y']


def check_password(login, password):
    login_without_vowel = list(filter(lambda a: a not in VOWEL, login))
    password_without_vowel = list(filter(lambda a: a not in VOWEL, password))
    if len(list(filter(lambda a: a in VOWEL, password))) == 3:
        if login_without_vowel == password_without_vowel:
            return 'OK'
        else:
            return 'Wrong consonants'
    elif len(list(filter(lambda a: a in VOWEL, password))) != 3 and login_without_vowel == password_without_vowel:
        return 'Wrong number of vowels'
    else:
        return 'Everything is wrong'


def ask_password(login, password, success, failure):
    login = login.lower()
    password = password.lower()
    message = check_password(login, password)
    if message == 'OK':
        success(login)
    else:
        failure(login, message)


def verification_successful(login):
    print(f"Привет, {login}!")


def verification_failed(login, err):
    print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.")


def main(login, password):
    success = verification_successful
    failure = verification_failed
    ask_password(login, password, success, failure)
