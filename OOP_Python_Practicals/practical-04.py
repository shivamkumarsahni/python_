# Practical 4: Character Classification
# Aim: To identify whether a character is a letter, digit, or special character, and display its case or digit name.

# Accept a character
ch = input("Enter a character: ")


if len(ch) != 1:
    print("Please enter only one character.")


# Check whether it is a letter
elif ch.isalpha():

    print("It is a letter.")

    if ch.isupper():
        print("It is an uppercase letter.")

    else:
        print("It is a lowercase letter.")


# Check whether it is a numeric digit
elif ch.isdigit() and ch.isascii():

    print("It is a numeric digit.")

    digit_names = [
        "ZERO", "ONE", "TWO", "THREE", "FOUR",
        "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
    ]

    print("Digit in words:", digit_names[int(ch)])


# Otherwise, it is a special character
else:
    print("It is a special character.")