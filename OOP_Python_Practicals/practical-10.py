# Practical 10: Dictionary of cubes from 1 to 5

# Create a dictionary where keys are numbers
# and values are cubes of those numbers

def create_dictionary():
    cubes = {}

    for number in range(1, 6):
        cubes[number] = number ** 3

    print("Dictionary of cubes:", cubes)


create_dictionary()