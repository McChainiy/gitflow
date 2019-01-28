class Point:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        self.name, self.x, self.y = name, x, y
        self.color = color

    def get_color(self):
        return self.color

    def __invert__(self):
        rev_color = tuple([255 - i for i in self.color])
        return ColoredPoint(self.name, self.y, self.x, rev_color)
