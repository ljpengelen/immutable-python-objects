from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def scale(self, scale):
        return Point(self.x * scale, self.y * scale)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
