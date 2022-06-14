class Balance:
    def __init__(self):
        self.weight_right = 0
        self.weight_left = 0

    def add_right(self, weight):
        self.weight_right += weight

    def add_left(self, weight):
        self.weight_left += weight

    def result(self):
        if self.weight_left == self.weight_right:
            return '='
        elif self.weight_left > self.weight_right:
            return 'L'
        return 'R'
