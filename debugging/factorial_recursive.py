#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a given number `n` using recursion.

    Parameters:
    n (int): The number for which the factorial is calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Getting the input number from command-line arguments
f = factorial(int(sys.argv[1]))

# Printing the result (factorial of the input number)
print(f)
