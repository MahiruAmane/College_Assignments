# Write a Python Program To Create a Class For Operator Overloading Which Adds Two Point Objects Where Point Has X & Y Values.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print(result)