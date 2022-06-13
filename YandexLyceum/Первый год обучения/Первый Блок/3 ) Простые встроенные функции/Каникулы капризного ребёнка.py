firstCity = input()
secondCity = input()
if(firstCity == "Тула" and (secondCity != "Тула" and secondCity != "Пенза")):
    print("ДА")
elif(secondCity == "Пенза" and (firstCity != "Тула" and firstCity != "Пенза")):
    print("ДА")
else:
    print("НЕТ")