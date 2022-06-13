login = input()
extraMail = input()
if("@" not in login and "@" in extraMail):
    print("OK")
elif("@" in login):
    print("Некорректный логин")
elif("@" not in extraMail):
    print("Некорректный адрес")