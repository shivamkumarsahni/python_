# Practical 6: Swap the first n characters of two strings

# Program to swap the first n characters of two strings

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
n = int(input("Enter the value of n: "))

if 0 <= n <= min(len(str1), len(str2)):
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]

    print("First string after swapping:", new_str1)
    print("Second string after swapping:", new_str2)
else:
    print("Invalid value of n.")