from PIL import Image


im = Image.open("image.jpg")
pixels = im.load()
x, y = im.size
full = x * y
r = 0
g = 0
b = 0
for i in range(x):
    for j in range(y):
        r += pixels[i, j][0]
        g += pixels[i, j][1]
        b += pixels[i, j][2]
print(r // full, g // full, b // full)