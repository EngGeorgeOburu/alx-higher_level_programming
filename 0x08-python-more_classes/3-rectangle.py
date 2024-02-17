#!/usr/bin/python3
"""
This module defines a rectangle class.
Attributes:
    -width (int): The width of the rectangle.
    -height (int): The height of the rectangle.
Methods:
    __init__(self, width=0, height=0):Initialize a new rectange instance
    width(self): Gets the width of the rectangle.
    width(self, value): Sets the new width of the rectangle.
    height(self): Gets the height of the rectangle.
    height(self, value):Sets the value of the rectangle.
    area(self): Calculates the area of the rectangle.
    perimeter(self):Calculates the perimeter of the rectangle
    __str__(self): Return a string representation of the rectangle.
"""


class Rectangle:
    """Class represents a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initiliaze a new rectangle instance
        Args:
            width(int):The width of the rectangle
            height(int):The height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle
        Args:
            value(int):The new width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
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
        Sets the height of the triangle.
        Args:
            value (int): The new height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigh must be > 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
        int The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            int: The are of the rectangle
        """
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """
        Returns a string represemtation.
        Returns:
            str: A tring As string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return (('#' * self._width + "\n")*self._height)[:-1]
