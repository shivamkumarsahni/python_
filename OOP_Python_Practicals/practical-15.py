def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError(
            "Name must not contain digits or special characters."
        )

    return name


try:
    name = input("Enter your name: ")
    valid_name = validate_name(name)
    print("Valid name:", valid_name)

except ValueError as e:
    print("Invalid input:", e)