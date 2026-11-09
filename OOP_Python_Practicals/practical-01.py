import cmath

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check whether the equation is quadratic
if a == 0:
    print("Not a quadratic equation.")

else:
    # Calculate the discriminant
    d = b ** 2 - 4 * a * c

    # Calculate the roots
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)

    # Display the roots
    print("Root 1 =", root1)
    print("Root 2 =", root2)