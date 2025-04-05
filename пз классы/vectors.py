class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, dot1: Dot, dot2: Dot):
        self.dot1 = dot1
        self.dot2 = dot2

    @property
    def x(self):
        return self.dot2.x - self.dot1.x

    @property
    def y(self):
        return self.dot2.y - self.dot1.y

    def __add__(self, other):
        coord1 = Dot(0, 0)
        coord2 = Dot(self.x + other.x, self.y + other.y)
        return Vector(coord2, coord1)

def Vvod(ind):
    coordinati = input( {ind})
    x, y = map(float, coordinati.split())
    return Dot(x, y)


p1 = Vvod(1)
p2 = Vvod(2)
p3 = Vvod(3)
p4 = Vvod(4)

vector1 = Vector(p1, p2)
vector2 = Vector(p3, p4)

rvector = vector1 + vector2
print(rvector.x, rvector.y)
