def ask_password():
    password = 'password'
    count_try = 0
    while True:
        string = input()
        if string == password and count_try < 3:
            print('Пароль принят')
            break
        else:
            count_try += 1
        if count_try == 3:
            print('В доступе отказано')
            break