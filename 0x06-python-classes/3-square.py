#!/usr/bin/python3
"""
Define a class.
Attributes:
     __size (int): The size of the circle.
Methods:
     __init__(self, size): Initializes a new square instance
     area(self): Calculates a new area.
"""


class Square:
    """ Initializes a new Square instance.
        Parameters:
        size (int): Size of the circle.
        raises:
        TypeError: If size is not an integer.
        ValueError: If size <= 0
    """
    def __init__(self, size=0):
        """
        Initiales a new square instance.
        Parameters:
        size (int): Size of the circle
        raises:
        TypeError:If size is not an integer
        ValueError: If size <= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a cirle
        Returns:
        int: Area of the circle
        """
        return self.__size * self.__size
