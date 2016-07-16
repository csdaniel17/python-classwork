## Print a Square

# Print an nxn square of * characters. You will prompt the user to enter the number n.

# Example: for n = 5, it should look like:

# ```
# *****
# *****
# *****
# *****
# *****
# ```

def print_square(n):
    for i in range(0, n):
        print "*" * n


## test before adding input functionality
# print_square(5)
# print_square(2)


n = int(raw_input("Enter a number: "))
print_square(n)
