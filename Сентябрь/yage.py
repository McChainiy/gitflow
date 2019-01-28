class Point:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, int(x), int(y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)


class CheckMark:
    def __init__(self, fp, sp, tp):
        self.points = [fp, sp, tp]
        self.kkf = (fp.y - sp.y) / (fp.x - sp.x) #y = x*k + b
        self.bkf = fp.y - (fp.x * self.kkf)

    def __bool__(self):
        coords = self.get_coords()
        if len(set(coords)) != len(coords):
            return False
        zzz = list(zip(coords[0], coords[1], coords[2]))
        if 1 == len(set(zzz[0])) or 1 == len(set(zzz[1])):
            return False
        if self.points[2].y == self.points[2].x * self.kkf + self.bkf:
            return False
        return True

    def get_coords(self):
        return [i.get_coords() for i in self.points]

    def __str__(self):
        pts = [i.name for i in self.points]
        return '{}{}{}'.format(pts[0], pts[1], pts[2])

    def __eq__(self, other):
        return self.get_coords() == other.get_coords() or\
               self.get_coords() == other.get_coords()[::-1]


A1 = Point('P1', -30, 20)
A2 = Point('P2', -10, -10)
A3 = Point('P3', -20, -30)
A4 = Point('P4', 20, -30)
A5 = Point('P5', 30, 20)
A6 = Point('P6', 10, 10)
A7 = Point('P7', 30, 30)

cm_a = CheckMark(A1, A2, A3)
cm_b = CheckMark(A3, A2, A4)
cm_c = CheckMark(A3, A2, A7)
cm_d = CheckMark(A4, A2, A3)
cm_e = CheckMark(A2, A6, A7)
cm_f = CheckMark(A7, A5, A6)
cm_g = CheckMark(A1, A1, A6)
cm_h = CheckMark(A4, A5, A4)
cm_i = CheckMark(A3, A3, A3)

print(bool(cm_a))
print(bool(cm_b))
print(bool(cm_c))
print(bool(cm_d))
print(bool(cm_e))
print(bool(cm_f))
print(bool(cm_g))
print(bool(cm_h))
print(bool(cm_i))