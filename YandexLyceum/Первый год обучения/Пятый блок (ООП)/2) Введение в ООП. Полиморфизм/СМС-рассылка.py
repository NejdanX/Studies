from copy import copy


class Person:
    def __init__(self, name, patr, surname, phones):
        self.name, self.patr, self.surname = name, patr, surname
        self.phones = copy(phones)

    def get_phone(self):
        if 'private' in self.phones:
            return self.phones['private']
        else:
            return

    def get_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patr

    def get_work_phone(self):
        if 'work' in self.phones:
            return self.phones['work']
        else:
            return
        pass

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.patr}! Примите участие в ' \
               f'нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name, type, phones, *person):
        self.name = name
        self.type = type
        self.phones = copy(phones)
        self.people = person

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for person in self.people:
            if 'work' in person.phones:
                return person.phones['work']
        return

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.type}'


def send_sms(*args):
    objects = args
    for obj in objects:
        if obj.get_phone() is None:
            print(f'Не удалось отправить сообщение абоненту: {obj.get_name()}')
            continue
        print(f'Отправлено СМС на номер {obj.get_phone()} с текстом: {obj.get_sms_text()}')


person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)