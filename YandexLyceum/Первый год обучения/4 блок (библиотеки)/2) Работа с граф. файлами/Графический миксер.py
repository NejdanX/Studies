from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    px = im.load()
    s, h = im.size
    for x in range(s // 2):
        for y in range(h):
            r, g, b = px[x, y]
            r1, g1, b1 = px[s // 2 + x, y]
            px[x, y] = r1, g1, b1
            px[s // 2 + x, y] = r, g, b
    im.save(output_file_name)