class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        if self.name < other.name:
            return True
        if self.name > other.name:
            return False
        if self.x < other.x:
            return True
        if self.x > other.x:
            return False
        if self.y < other.y:
            return True
        if self.y > other.y:
            return False
        return False

    def __gt__(self, other):
        if self != other:
            return not(self < other)
        return False

    def __le__(self, other):
        if self == other:
            return True
        return self < other

    def __ge__(self, other):
        if self == other:
            return True
        return self > other

    def __str__(self):
        return f'{self.name}{self.get_coords()}'

    def __repr__(self):
        return f'Point(\'{self.name}\', {self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class CheckMark:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return self.a.name + self.b.name + self.c.name

    def __bool__(self):
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return False
        first = self.a.x * self.b.y + self.b.x * self.c.y + self.c.x * self.a.y
        second = self.b.x * self.a.y + self.c.x * self.b.y + self.a.x * self.c.y
        return bool(first - second)

    def __eq__(self, other):
        h = (self.a.x == other.c.x and self.a.y == other.c.y)
        first = (self.a.x == other.a.x and self.a.y == other.a.y) or h
        second = (self.b.x == other.b.x and self.b.y == other.b.y)
        third = (self.c.x == other.c.x and self.c.y == other.c.y) or h
        return first and second and third


p_A = Point('A', 1, 2)
p_B = Point('B', 0, 1)
p_C = Point('C', -1, 2)
p_D = Point('D', -1, 2)
cm_ABC = CheckMark(p_A, p_B, p_C)
cm_CBA = CheckMark(p_C, p_B, p_A)
cm_ACB = CheckMark(p_A, p_C, p_B)
cm_ABD = CheckMark(p_A, p_B, p_D)
cm_DBA = CheckMark(p_D, p_B, p_A)
print(cm_ABC == cm_CBA, cm_ABC == cm_ABD)
print(cm_ABC == cm_DBA, cm_ABC == cm_ACB)