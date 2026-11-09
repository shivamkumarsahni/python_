# Practical 7: Find all indices of the second string in the first string

# Function to find all occurrences of a substring

def find_indices(string1, string2):
    indices = []

    if string2 == "":
        return indices

    start = 0

    while True:
        index = string1.find(string2, start)

        if index == -1:
            break

        indices.append(index)
        start = index + 1

    if len(indices) == 0:
        return -1

    return indices


# Main program
text = input("Enter the first string: ")
substring = input("Enter the second string: ")

result = find_indices(text, substring)

print("Result:", result)