# Practical 9: Read a file and perform different operations

# File handling in Python

filename = input("Enter the file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # (a) Count characters, words and lines
    characters = len(content)
    words = len(content.split())
    lines = len(content.splitlines())

    print("\n(a) File Statistics")
    print("Total characters:", characters)
    print("Total words:", words)
    print("Total lines:", lines)

    # (b) Frequency of each character
    frequency = {}

    for character in content:
        frequency[character] = frequency.get(character, 0) + 1

    print("\n(b) Character Frequency")

    for character, count in frequency.items():
        if character == "\n":
            print("Newline:", count)
        elif character == " ":
            print("Space:", count)
        else:
            print(repr(character) + ":", count)

    # (c) Print words in reverse order
    word_list = content.split()

    print("\n(c) Words in Reverse Order")
    print(" ".join(word_list[::-1]))

    # (d) Copy even lines to File1 and odd lines to File2
    with open(filename, "r", encoding="utf-8") as file:
        file_lines = file.readlines()

    with open("File1.txt", "w", encoding="utf-8") as file1, \
         open("File2.txt", "w", encoding="utf-8") as file2:

        for line_number, line in enumerate(file_lines, start=1):
            if line_number % 2 == 0:
                file1.write(line)
            else:
                file2.write(line)

    print("\n(d) File copying completed.")
    print("Even lines copied to File1.txt")
    print("Odd lines copied to File2.txt")

except FileNotFoundError:
    print("File not found. Please check the file name.")