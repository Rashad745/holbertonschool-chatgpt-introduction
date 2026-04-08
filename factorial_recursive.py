#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a number using recursion.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: Factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate factorial of the number passed as the first command line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
