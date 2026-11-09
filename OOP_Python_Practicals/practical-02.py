# Practical 2: Prime Numbers Using Functions
# Aim: To check whether a number is prime, generate all prime numbers up to n, and generate the first n prime numbers.

# Function to check prime number
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            return False

    return True


n = int(input("Enter a number: "))


# (a) Check whether n is prime
if is_prime(n):
    print(n, "is a prime number.")

else:
    print(n, "is not a prime number.")


# (b) Generate all prime numbers up to n
print("Prime numbers up to", n, ":")

for i in range(2, n + 1):

    if is_prime(i):
        print(i, end=" ")

print()


# (c) Generate the first n prime numbers
print("First", n, "prime numbers:")

count = 0
num = 2

while count < n:

    if is_prime(num):
        print(num, end=" ")
        count += 1

    num += 1

print()