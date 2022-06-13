contacts = {}
for _ in range(int(input())):
    contact = input()
    number, name = contact[:contact.find(' ')], contact[contact.find(' ') + 1:]
    if(name in contacts):
        contacts[name] += number + ' '
    else:
        contacts[name] = number + ' '
for _ in range(int(input())):
    number = contacts.get(input(), "Нет в телефонной книге.")
    print(number[:len(number) - 1])
    