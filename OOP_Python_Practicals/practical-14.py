# Practical 14: Inherit 2DPoint to create a 3DPoint class

# Practical 14: Three-dimensional point using inheritance

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point: ({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
        )


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # Override the display method
    def display(self):
        print(f"Point: ({self.x}, {self.y}, {self.z})")

    # Override the distance method
    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )


# Create two 3D points
p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 6, 3)

p1.display()
p2.display()

print("Distance between points:", p1.distance(p2))