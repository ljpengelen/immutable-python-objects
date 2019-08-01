import attr


@attr.s(frozen=True)
class Point:
    x = attr.ib()
    y = attr.ib()

    def scale(self, scale):
        return Point(self.x * scale, self.y * scale)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
