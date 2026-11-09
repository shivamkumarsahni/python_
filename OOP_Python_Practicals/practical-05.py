# Practical 5: String Operations
# Aim: To find the frequency of a character, replace a character, remove its first occurrence, and remove all occurrences.

# Accept a string
s = input("Enter a string: ")

# Accept the character to search
ch = input("Enter the character to search: ")


# (a) Find frequency
frequency = s.count(ch)

print("Frequency:", frequency)


# (b) Replace a character
new_ch = input("Enter the replacement character: ")

result = s.replace(ch, new_ch)

print("After replacement:", result)


# (c) Remove the first occurrence
result = s.replace(ch, "", 1)

print("After removing first occurrence:", result)


# (d) Remove all occurrences
result = s.replace(ch, "")

print("After removing all occurrences:", result)