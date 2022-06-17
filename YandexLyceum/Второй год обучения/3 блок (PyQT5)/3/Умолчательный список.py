class DefaultList(list):
    def __init__(self, default_value):
        super(DefaultList, self).__init__()
        self.default_value = default_value

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return self.default_value


s = DefaultList(51)
s.extend([1, 5, 7])

indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")