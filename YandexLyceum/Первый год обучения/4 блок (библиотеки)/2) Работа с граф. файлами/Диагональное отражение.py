from PIL import Image


def mirror():
    im = Image.open("image2.jpg")
    im = im.rotate(270).transpose(Image.FLIP_TOP_BOTTOM)
    im.save('res.png')
