emails = [input() for _ in range(int(input()))]
new_employees = [input() for _ in range(int(input()))]
end_mail = '@untitled.py'
for employee in new_employees:
    for i in range(len(emails) - 1, -1, -1):
        if employee in emails[i]:
            number = emails[i][len(employee):emails[i].find('@')]
            if number:
                number = int(number) + 1
            else:
                number = 1
            new_mail = employee + str(number) + end_mail
            print(new_mail)
            emails.append(new_mail)
            break
    else:
        new_mail = employee + end_mail
        print(new_mail)
        emails.append(new_mail)