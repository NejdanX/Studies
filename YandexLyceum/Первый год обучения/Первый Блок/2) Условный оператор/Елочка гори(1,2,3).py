firstStr = input()
secondStr = input()
thirdStr = input()
result = firstStr + secondStr + thirdStr
if((firstStr == "раз" or firstStr == "один") and secondStr == "два" and thirdStr == "три"):
    print("ГОРИ")
elif(firstStr == "1" and secondStr == "2" and thirdStr == "3"):
    print("ГОРИ")
else:
    print("НЕ ГОРИ")