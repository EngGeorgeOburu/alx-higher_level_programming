#!/usr/bin/python3
"""
This is module 10-sqaure.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square with given size.
        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

