#!/usr/bin/python3
# Importing the add function from add_0.py
from add_0 import add

# This is the add function that performs addition
def add(a, b):
    return a + b

# Assigning values to variables a and b
a = 1
b = 2

# Calling the add function with a and b as arguments
result = add(a, b)

# Printing the result with string formatting
print(f"{a} + {b} = {result}" end="\n")
