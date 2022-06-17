from PIL import Image
import numpy as np

def image_filter(pixels, i, j, step):
    r = (pixels[j, ::step, 0].min() + pixels[j, i, 0]) % 255
    g = (pixels[j, ::step, 1].min() + pixels[j, i, 1]) % 255
    b = (pixels[j, ::step, 2].min() + pixels[j, i, 2]) % 255
    return r, g, b


im = Image.open('Прозрачность/bbbb.jpg')
pix = im.load()
x, y = im.size
np_pixels = np.array(im)
for i in range(x):
    for j in range(y):
        pix[i, j] = image_filter(np_pixels, i, j, 500)
im.save('res.jpg')