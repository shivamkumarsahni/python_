# Practical 13: Create a 2DPoint class

# Practical 13: Two-dimensional point

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point: ({self.x}, {self.y})")

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return math.sqrt(dx ** 2 + dy ** 2)


# Create two point objects
p1 = Point2D(3, 4)
p2 = Point2D(6, 8)

p1.display()
p2.display()

print("Distance between points:", p1.distance(p2))