import math


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        # self.other = {"a": 1, "b": 2}

    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        return Vector(self.x * other, self.y * other)

    def __repr__(self):
        return f"Vector({self.x!r},{self.y!r})"

    def __getattr__(self, name):
        print("invoke __getattr__ method")
        return "not exists"


v1 = Vector(1, 2)
# v2=Vector(3,4)
# print(v1+v2)
# print(abs(v2))
# print(v2*3)
print(v1.a)
