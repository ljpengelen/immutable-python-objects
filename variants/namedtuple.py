from collections import namedtuple


class Point(namedtuple("_Point", ["x", "y"])):
    def scale(self, scale):
        return Point(self.x * scale, self.y * scale)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
