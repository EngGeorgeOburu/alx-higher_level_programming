#!/usr/bin/python3
"""
Define a class representing a Square.
Atributes:
    __size (int):Size of the square.
Methods:
    __init__(self, size=0): Initializes a new square instance
    size(self): Getter method for retreiving the  size of a square.
    size(self, value): Setter method for setting new size of the square.
    area(self): Calculates the area of a square.
"""


class Square:
    """
    Initializes a new square instance.
    raises:
    TypeError: If size is not an integer
    ValueError: If size is less than 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """ set the sizeattribute """
        self.__size = size
    """
    Getter method for retriving size of the square
    Returns:
        int: size of the  square
    """
    @property
    def size(self):
        return self.__size
    """
    Setter method for setting size of the square.
    Parameters:
    int: New size of the square
    Raises:
    TypeError: if size is not an integer.
    ValueError: If size is less than 0
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be an interger")
        # Set size o attribute """
        self.__size = value

    """
    Calculates the error of a new square
    Returns:
    int: Area of the square
    """

    def area(self):
        return self.__size ** 2
