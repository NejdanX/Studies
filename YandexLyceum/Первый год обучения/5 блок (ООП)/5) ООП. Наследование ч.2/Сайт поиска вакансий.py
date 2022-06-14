class Profile:
    def __init__(self, name_prof):
        self.name_prof = name_prof

    def info(self):
        return ''

    def describe(self):
        print(f'{self.name_prof}\n{self.info()}')


class Vacancy(Profile):
    def __init__(self, name_prof, salary):
        super().__init__(name_prof)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'


class Resume(Profile):
    def __init__(self, name_prof, background):
        super().__init__(name_prof)
        self.background = background

    def info(self):
        return f'Стаж работы: {self.background}'
