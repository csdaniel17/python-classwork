## Print a Box

# Given a height and width, print a box consisting of * characters as its border. You will prompt the user to enter the height and width.

# Example: given the height of 4 and the width of 6, you should print:

# ```
# ******
# *    *
# *    *
# ******
# ```

def print_box(h, w):
    print "*" * w

    for i in range(0, h - 2):
        print "*" + (" " * (w - 2)) + "*"

    print "*" * w

## test before adding input functionality
# print_box(4, 6)
# print_box(6, 4)
# print_box(5, 5)

h = int(raw_input("Enter a height: "))
w = int(raw_input("Enter a width: "))
print_box(h, w)


# version 2 #
def print_box2(h, w):
    for i in range(0, h):
        if i == 0 or i == h - 1:
            print "*" * w
        else:
            print "*" + (" " * (w - 2)) + "*"

h = int(raw_input("Enter a height: "))
w = int(raw_input("Enter a width: "))
print_box2(h, w)
