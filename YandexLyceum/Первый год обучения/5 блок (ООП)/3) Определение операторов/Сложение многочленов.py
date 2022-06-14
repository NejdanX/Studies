class Polynomial:
    def __init__(self, coef):
        self.coefficients = coef

    def __call__(self, *args, **kwargs):
        x = args[0]
        result = 0
        for i in range(len(self.coefficients)):
            result += (self.coefficients[i] * x ** i)
        return result

    def __add__(self, other):
        min_len = min(len(self.coefficients), len(other.coefficients))
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_list = []
        for i in range(min_len):
            result_list.append(self.coefficients[i] + other.coefficients[i])
        result_list += (self.coefficients[min_len:max_len] + other.coefficients[min_len:max_len])
        return Polynomial(result_list)
