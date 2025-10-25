#!/usr/bin/python3
"""
This program calculates the factorial of a number using recursion.
A factorial is the product of all positive integers less than or equal to n.
For example: 4! = 4 × 3 × 2 × 1 = 24
"""
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    The factorial of a non-negative integer n is the product of all positive 
    integers less than or equal to n. It is denoted by n! and defined as:
    - 0! = 1 (by definition)
    - n! = n × (n-1) × (n-2) × ... × 1 for n > 0
    
    This function uses recursion by calling itself with (n-1) until it 
    reaches the base case of n = 0.
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.
             Must be >= 0. If n is 0, the function returns 1.
    
    Returns:
    int: The factorial of n. Returns 1 if n is 0, otherwise returns
         n multiplied by the factorial of (n-1).
    
    Examples:
    factorial(0) returns 1
    factorial(4) returns 24 (4 × 3 × 2 × 1)
    factorial(5) returns 120 (5 × 4 × 3 × 2 × 1)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)