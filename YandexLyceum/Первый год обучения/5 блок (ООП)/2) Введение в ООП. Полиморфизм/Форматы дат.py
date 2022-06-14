class AmericanDate:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        self.month = str(self.month)
        self.day = str(self.day)
        return f'{self.month.rjust(2, "0")}.{self.day.rjust(2, "0")}.{self.year}'


class EuropeanDate:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        self.month = str(self.month)
        self.day = str(self.day)
        return f'{self.day.rjust(2, "0")}.{self.month.rjust(2, "0")}.{self.year}'
