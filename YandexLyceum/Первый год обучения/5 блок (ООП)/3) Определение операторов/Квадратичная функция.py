class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, *args, **kwargs):
        x = args[0]
        return self.a * x ** 2 + self.b * x + self.c
