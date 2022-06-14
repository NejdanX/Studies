import math


def square_ellipse(a, b):
    return math.pi * a * b


def find_farthest_orbit(list_of_orbits):
    orbits = [item for item in list_of_orbits if item[0] != item[1]]
    max_square = 0
    num = 0
    for i in range(len(orbits)):
        square = square_ellipse(orbits[i][0], orbits[i][1])
        if max_square < square:
            max_square = square
            num = i
    return orbits[num]
