PI = 3.14159


def circle_length(radius):
    return 2 * PI * radius


def circle_area(radius):
    return PI * radius ** 2


def main():
    r = float(input())
    print(circle_length(r), circle_area(r))
