from PIL import ImageDraw, Image


class Drawer:
    def __init__(self, draw_map, cell_size):
        colors = {}
        self.color_numbers = {}
        self.draw_map = draw_map
        self.cell_size = cell_size
        for num in self.numbers():
            self.color_numbers[num] = colors.get(num, 'black')

    def numbers(self):
        flat_list = list(set([item for sublist in self.draw_map for item in sublist]))
        return sorted(flat_list)

    def set_color(self, number, color):
        self.color_numbers[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        return self.cell_size * len(self.draw_map[0]), self.cell_size * len(self.draw_map)

    def draw(self):
        new_image = Image.new("RGB", self.size(), (0, 0, 0))
        drawer = ImageDraw.Draw(new_image)
        y = 0
        for i in range(len(self.draw_map)):
            x = 0
            for j in range(len(self.draw_map[i])):
                drawer.rectangle(((x, y), (x + self.cell_size, y + self.cell_size)),
                                 fill=self.color_numbers[self.draw_map[i][j]])
                x += self.cell_size
            y += self.cell_size
        return new_image
