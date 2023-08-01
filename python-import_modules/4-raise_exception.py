def raise_exception():
    raise TypeError("This is a type exception")

# Test the function
try:
    raise_exception()
except TypeError as e:
    print("Exception caught:", e)
