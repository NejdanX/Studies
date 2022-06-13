class Rectangle:
    def __init__(self, x_d, y_d, w, h):
        self.x_down = x_d
        self.y_down = y_d
        self.w = w
        self.h = h
        self.x_up = self.x_down + self.w
        self.y_up = self.y_down + self.h

    def intersection(self, rect):
        if rect.x_down >= self.x_up or rect.y_down >= self.y_up \
                or self.x_down >= rect.x_up or self.y_down >= rect.y_up:
            return
        else:
            x = max(self.x_down, rect.x_down)
            w = min(self.x_up, rect.x_up) - x
            y = max(self.y_down, rect.y_down)
            h = min(self.y_up, rect.y_up) - y
            res = Rectangle(x, y, w, h)
            return res

    def get_x(self):
        return self.x_down

    def get_y(self):
        return self.y_down

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h
