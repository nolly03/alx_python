def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        print("Inside result: {}".format(result))

    return result

# Test cases
print(safe_print_division(10, 2))
print(safe_print_division(10, 0))
print(safe_print_division(10, '2'))  # This will raise an exception and print the error message
