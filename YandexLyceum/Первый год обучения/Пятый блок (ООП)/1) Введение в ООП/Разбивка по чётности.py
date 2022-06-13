class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def odd(self):
        return list(filter(lambda x: x % 2 == 1, self.numbers))

    def even(self):
        return list(filter(lambda x: x % 2 == 0, self.numbers))
