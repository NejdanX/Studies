class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(f'{self.name}\n{self.info()}')


class Person(User):
    def __init__(self, name, date):
        super().__init__(name)
        self.date = date

    def info(self):
        return f'Дата рождения: {self.date}'

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, desc):
        super().__init__(name)
        self.desc = desc

    def info(self):
        return f'Описание: {self.desc}'
