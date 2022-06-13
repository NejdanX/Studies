password = int(input())
amountSenior = password // 100 + (password % 100) // 10
amountJunior = (password % 100) // 10 + password % 10
if(amountSenior > amountJunior):
    print(str(amountSenior) + str(amountJunior))
else:
    print(str(amountJunior) + str(amountSenior))
    