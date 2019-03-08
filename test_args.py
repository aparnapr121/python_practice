print("*** Exceptions ***")
class TriangleError(Exception):
    def __init__(self, message, sides):
        super().__init__(message)
        self.message = message
        self._sides = sides
        print("args", self.args)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return f"{self.text} for sides {self.sides}"

    def __repr__(self):
        return f"Triangle Error here"

def perimeter(a,b,c):
    sides =sorted((a,b,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    return a+b+c
perimeter(3,4,9)