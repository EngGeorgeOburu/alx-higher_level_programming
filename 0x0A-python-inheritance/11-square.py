#!/usr/bin/python3
"""
This is module 11 representing 11-square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square, inherits from a triangle.
    """

    def __init__(self, size):
        """
        Initializesa square with the given size.
        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[square] {}/{}".format(self.__width, self.__height)
