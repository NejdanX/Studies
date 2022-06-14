class BoundingRectangle:
    def __init__(self):
        self.coordinates = []

    def add_point(self, x, y):
        self.coordinates.append((x, y))

    def width(self):
        x = [i[0] for i in self.coordinates]
        return max(x) - min(x)

    def height(self):
        y = [i[1] for i in self.coordinates]
        return max(y) - min(y)

    def bottom_y(self):
        return min([i[1] for i in self.coordinates])

    def top_y(self):
        return max([i[1] for i in self.coordinates])

    def left_x(self):
        return min([i[0] for i in self.coordinates])

    def right_x(self):
        return max([i[0] for i in self.coordinates])
