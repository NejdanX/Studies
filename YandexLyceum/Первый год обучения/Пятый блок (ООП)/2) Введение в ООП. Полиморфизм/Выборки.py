from copy import copy


class Selector:
    def __init__(self, numbers):
        self.numbers = copy(numbers)

    def get_odds(self):
        return list(filter(lambda x: x % 2 == 1, self.numbers))

    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.numbers))
