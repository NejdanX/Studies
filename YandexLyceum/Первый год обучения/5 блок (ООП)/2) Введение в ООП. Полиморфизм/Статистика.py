class MinStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def result(self):
        if self.numbers:
            return min(self.numbers)
        return None


class MaxStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def result(self):
        if self.numbers:
            return max(self.numbers)
        return None


class AverageStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def result(self):
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        return None
