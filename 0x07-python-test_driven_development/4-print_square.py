#!/usr/bin/python3

def print_square(size):
    """
    Prints squares of '#' characters.
    Args:
        size (int): The size of the square.
    Raises:
        TypeError:If size is not an integer.
        ValueError: If size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
