class Button:
    def __init__(self):
        self.cl = 0

    def click(self):
        self.cl += 1

    def click_count(self):
        return self.cl

    def reset(self):
        self.cl = 0
