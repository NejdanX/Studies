from PIL import Image, ImageDraw


def triangle(width, height, color):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.polygon([(int(width * 0.5), int(height * 0.2)),
                   (width * 0.9, height * 0.9), (width * 0.1, height * 0.9)],
                   color)

    im.save('triangle.png')


triangle(100, 100, '#F443AF')