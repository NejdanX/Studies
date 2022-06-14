def larger_root(p, q):
    D = discriminant(1, p, q)
    x1 = (-p + D ** (1 / 2)) / 2
    x2 = (-p - D ** (1 / 2)) / 2
    if x1 > x2:
        return x1
    return x2


def smaller_root(p, q):
    D = discriminant(1, p, q)
    x1 = (-p + D ** (1 / 2)) / 2
    x2 = (-p - D ** (1 / 2)) / 2
    if x1 < x2:
        return x1
    return x2
    pass


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(f"{smaller_root(p, q)} {larger_root(p, q)}")
