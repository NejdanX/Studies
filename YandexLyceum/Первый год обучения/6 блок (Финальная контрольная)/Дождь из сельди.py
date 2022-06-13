from PIL import Image, ImageDraw


class FishImageDraw(ImageDraw.ImageDraw):
    def __init__(self, obj):
        self.obj = ImageDraw.Draw(obj)

    def fish(self, xy, fill):
        x = xy[0]
        y = xy[1]
        w = xy[2]
        d = xy[3]
        self.obj.rectangle(((x + w // 2 - d, y - d // 4), (x + w // 2 + d, y + d // 2)), fill[2])
        self.obj.ellipse((x, y, x + w, y + d // 2 * 3), fill=fill[0])
        self.obj.ellipse((x + d - d // 4, y + d // 2 * 3 // 2 - d // 4,
                          x + d + d // 4, y + d // 2 * 3 // 2 + d // 4), fill[1])
        self.obj.polygon([(x + w, y + d // 2 * 3 // 2),
                          (x + w + d, y), (x + w + d, y + d // 2 * 3)], fill=fill[2])
