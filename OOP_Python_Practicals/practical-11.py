# Practical 11: Perform operations on a tuple

# Perform different operations on a tuple

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# (a) Print half the values on each line
middle = len(t1) // 2

print("First half:", t1[:middle])
print("Second half:", t1[middle:])

# (b) Print even numbers in a new tuple
even_numbers = tuple(
    number for number in t1 if number % 2 == 0
)

print("Even numbers:", even_numbers)

# (c) Concatenate t2 with t1
t2 = (11, 13, 15)
combined = t1 + t2

print("Concatenated tuple:", combined)

# (d) Find maximum and minimum values
print("Maximum value:", max(t1))
print("Minimum value:", min(t1))