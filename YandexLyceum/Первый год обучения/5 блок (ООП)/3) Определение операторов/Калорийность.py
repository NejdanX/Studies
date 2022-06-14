class FoodInfo:
    def __init__(self, p, f, c):
        self.proteins = p
        self.fats = f
        self.carbohydrates = c

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates

    def __add__(self, other):
        p = self.proteins + other.proteins
        f = self.fats + other.fats
        c = self.carbohydrates + other.carbohydrates
        return FoodInfo(p, f, c)
