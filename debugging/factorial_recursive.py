#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
    n (int): The integer to calculate the factorial of.

    Returns:
    int: The calculated factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)