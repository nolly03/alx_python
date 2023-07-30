import sys

def main():
    argv = sys.argv[1:]  # Exclude the first argument, which is the script filename

    # Print the number of arguments
    num_args = len(argv)
    print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}:")
    
    # If at least one argument is present, print them one by one
    if num_args > 0:
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
