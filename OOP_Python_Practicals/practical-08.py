# Practical 8: Cubes of even integers using a for loop and list comprehension

# (a) Cubes of even integers using a for loop

data = [2, 3, 4, "hello", 6, 7, 8.5, 10]

result = []

for item in data:
    if type(item) == int and item % 2 == 0:
        result.append(item ** 3)

print("Original list:", data)
print("Cubes of even integers:", result)

# (b) Cubes of even integers using list comprehension

data = [2, 3, 4, "hello", 6, 7, 8.5, 10]

result = [
    item ** 3
    for item in data
    if type(item) == int and item % 2 == 0
]

print("Original list:", data)
print("Cubes of even integers:", result)