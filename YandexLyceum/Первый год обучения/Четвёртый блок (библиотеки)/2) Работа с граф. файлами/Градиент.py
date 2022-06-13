from PIL import ImageDraw, Image


def gradient(color):
    color = color.upper()
    x_size = 512
    y_size = 200
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(y_size):
        for j in range(0, x_size, 2):
            if color == 'R':
                new_color = (j // 2, 0, 0)
            elif color == 'G':
                new_color = (0, j // 2, 0)
            else:
                new_color = (0, 0, j // 2)
            draw.line((j, i, j + 2, i), fill='blue', width=2)
    new_image.save('res.png')


gradient('red')
