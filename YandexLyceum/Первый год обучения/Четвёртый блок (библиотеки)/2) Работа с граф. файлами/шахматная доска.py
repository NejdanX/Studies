from PIL import Image, ImageDraw


def board(num, size):
    begin_color = (0, 0, 0)
    new_image = Image.new("RGB", (size * num, size * num), begin_color)
    draw = ImageDraw.Draw(new_image)
    x = 0
    y = 0
    for i in range(num + 1):
        for j in range(num + 1):
            if i % 2 == 0 and j % 2 != 0 or i % 2 != 0 and j % 2 == 0:
                draw.rectangle([(x, y), (x + size, y + size)], fill='#FFFFFF')
            x += size
        y += size
        x = 0
    new_image.save('result.png')


board(8, 50)