#!/usr/bin/python3
"""
Representing a rectangle class
Attributes:
    -width (int): The width of the rectangle.
    -height (int): The height of the rectangle.
Methods:
    __init__(self, width=0, height=0):Initialize \
            a new rectangle
    width(self):Gets the width of the rectangle.
    width(self, value):Sets the width of the rectangle
    height(self):Gets the height of the rectangle.
    height(self, value):Sets the height of the rectangle
    area(self):Calculates the area of the rectangle
    perimeter(self):Calculator and returns the perimeter of the rectangle.
    """


class Rectangle:
    """Class represents a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            -width (int): The width of the rectangle.
            -height (int): The heighht of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        returns:
        int: the width of the rectangle
        return self._width
        """

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Args:
            Value (int): new width
        Raises:
        TypeError: if number is not integer
        ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        Returns:
        int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
         Args:
        value (int): The new height value.
         Raises:
         TypeError:if value is not integer
         ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Returns:
        int: The area of the rectangle
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter
        Returns:
        int: perimeter
        """
        if self._height == 0 or self._width == 0:
            return 0
        return (self._width * 9) + (self._height * 2)
