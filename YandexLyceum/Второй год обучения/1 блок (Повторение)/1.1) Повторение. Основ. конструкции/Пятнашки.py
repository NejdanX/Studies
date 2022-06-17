from PIL import Image

im = Image.open('image.png')
pixels = im.load()
x, y = im.size
x1, y1 = 0, 0
for i in range(1, 5):
    for j in range(1, 5):
        if i == 4 and j == 4:
            break
        image = im.crop((x1, y1, x1 + x / 4, y1 + y / 4))
        image.save('image{}{}.bmp'.format(i, j))
        x1 += (x / 4)
    y1 += (y / 4)
    x1 = 0


