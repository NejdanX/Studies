class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        amount = 0
        for i in range(1, N + 1):
            amount += self.transform(i)
        return amount


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
