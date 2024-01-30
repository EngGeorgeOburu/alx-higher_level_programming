#!usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers
    Args:
        a (int or float): The first integer or float.
        b (int or float): The second integer or float.
    Return:
    int: The sum of a + b
    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
