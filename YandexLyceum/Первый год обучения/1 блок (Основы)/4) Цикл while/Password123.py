password = input()
if(len(password) < 8):
    print("Короткий!")
else:
    enterPassword = input()
    if(enterPassword == password):
        print("OK")
    else:
        print("Различаются.")
    