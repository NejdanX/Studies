message = input()
paid = len(message) * 0.4
print(int(paid), "р.", round(paid % 1 * 100), "коп.")