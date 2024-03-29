#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # Check if it's the last element in the row
            if i != len(row) - 1:
                # Adds a space after each number
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print()  # Move to the next line after a complete row
