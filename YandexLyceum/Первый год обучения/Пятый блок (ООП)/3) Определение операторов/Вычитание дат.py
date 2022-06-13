import datetime
COUNT_DAY_IN_MONTH = [(1, 30), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30),
                      (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]


class Date:
    def __init__(self, m, d):
        self.date = datetime.datetime(2019, m, d)

    def __sub__(self, other):
        delta_time = self.date - other.date
        return delta_time.days
