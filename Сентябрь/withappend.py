class Point:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        return "Point('{}', {}, {})".format(self.name, self.x, self.y)

    def __lt__(self, other):
        if self.name > other.name:
            return False
        elif self.name < other.name:
            return True
        if self.x > other.x:
            return False
        elif self.x < other.x:
            return True
        if self.y >= other.y:
            return False
        return True

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        return True

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return self > other or self == other

    def __gt__(self, other):
        if self.name < other.name:
            return False
        elif self.name > other.name:
            return True
        if self.x < other.x:
            return False
        elif self.x > other.x:
            return True
        if self.y <= other.y:
            return False
        return True

    def __hash__(self):
        return int('{}{}{}{}'.format(hash(self.name), len(str(hash(self.name))),
                                     self.x + len(str(self.x)) if self.x > 0 else
                                     str(self.x)[1:] + str(len(str(self.x))),
                                     self.y + len(str(self.y)) if self.y > 0 else
                                     str(self.y)[1:] + str(len(str(self.y)))))


print(hash('A'))
print(hash(Point('A', 1, -123)))