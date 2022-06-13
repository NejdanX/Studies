def pow_2(a, b, c):
    D = discriminant(a, b, c)
    if D < 0:
        return 0, 0
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    x2 = (-b - D ** (1 / 2)) / (2 * a)
    return x1, x2


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solve(*coefficients):
    if len(coefficients) == 3:
        x1, x2 = pow_2(*coefficients)
        if x1 == x2 == 0:
            return []
        elif x1 == x2:
            return [x1]
        return [x1, x2]
    elif len(coefficients) == 2:
        return [-coefficients[1] / coefficients[0]]
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['all']
        return []
    return
