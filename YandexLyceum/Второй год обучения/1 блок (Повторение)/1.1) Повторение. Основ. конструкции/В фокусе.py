from PIL import Image

im = Image.open('image1.png')
pixels = im.load()
x, y = im.size
cropped = im.crop((250, 100, 400, 250))
cropped.save('res1.png')