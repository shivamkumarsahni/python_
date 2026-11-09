n = int(input("Enter the number of rows: "))


# Print pyramid
print("Pyramid:")

for i in range(1, n + 1):

    spaces = " " * (n - i)
    stars = "* " * i

    print(spaces + stars)


# Print reverse pyramid
print("Reverse Pyramid:")

for i in range(n, 0, -1):

    spaces = " " * (n - i)
    stars = "* " * i

    print(spaces + stars)
    