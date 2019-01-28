class Point:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)
