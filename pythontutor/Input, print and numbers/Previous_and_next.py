"""
Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the
exact format your answers should take. There shouldn't be a space before the period. Remember that you can convert the
numbers to strings using the function str.
"""

number = int(input())

print("The next number for the number {} is {}".format(number, number + 1))
print("The previous number for the number {} is {}".format(number, number - 1))
