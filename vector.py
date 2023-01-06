from math import sqrt


class Vector:

    def __init__(self, x=0., y=0.):
        self.x = float(x)
        self.y = float(y)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError("Out of index (Vector)")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Out of index (Vector)")

    # Addition
    def __add__(self, rhs):
        x = self.x + rhs
        y = self.y + rhs
        return Vector(x, y)

    def __iadd__(self, rhs):
        self.x += rhs
        self.y += rhs
        return self

    def __radd__(self, lhs):
        x = self.x + lhs
        y = self.y + lhs
        return Vector(x, y)

    # Subtration
    def __sub__(self, rhs):
        x = self.x - rhs
        y = self.y - rhs
        return Vector(x, y)

    def __isub__(self, rhs):
        self.x -= rhs
        self.y -= rhs
        return self

    def __rsub__(self, lhs):
        x = self.x - lhs
        y = self.y - lhs
        return Vector(x, y)

    # Multiplication
    def __mul__(self, rhs):
        x = self.x * rhs
        y = self.y * rhs
        return Vector(x, y)

    def __imul__(self, rhs):
        self.x *= rhs
        self.y *= rhs
        return self

    def __rmul__(self, lhs):
        x = self.x * lhs
        y = self.y * lhs
        return Vector(x, y)

    # Division
    def __div__(self, rhs):
        x = self.x / rhs
        y = self.y / rhs
        return Vector(x, y)

    def __idiv__(self, rhs):
        self.x /= rhs
        self.y /= rhs
        return self

    def __rdiv__(self, lhs):
        x = lhs / self.x
        y = lhs / self.y
        return Vector(x, y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    # Length Property
    def _get_length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def _set_length(self, length):
        try:
            length_increase = length / self.length
        except ZeroDivisionError:
            return self
        self.x *= length_increase
        self.y *= length_increase
    length = property(_get_length, _set_length)
    get_length = _get_length

    def normalise(self):
        try:
            self.x /= self.length
            self.x /= self.length
        except ZeroDivisionError:
            self.x = 0.
            self.y = 0.
        return self

    def get_normalised(self):
        x = self.x
        y = self.y
        length = self.length
        return Vector(x / length, y / length)

    def get_distance_to(self, p):
        x1, x2 = p
        dx = x1 - self.x
        dy = x2 - self.y
        return sqrt(dx ** 2 + dy ** 2)

    def cross_product_2d(self, other):
        cross_product = self.x * other.y - self.y * other.x
        return cross_product

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    x1, y1 = v2
    print(x1, y1)
    v2 = v2 / 4
    print(v2)