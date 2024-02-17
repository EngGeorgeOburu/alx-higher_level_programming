#!/usr/bin/python3
"""
This module defines a rectangle class.
Attributes:
    -width (int): Widht of the rectangle
    -height (int): Height of the rectangle
Methods:
    __init__(self, width=0, height=0): Initializes a new rectangle.
    width (self): Gets the width of the rectangle
    width (self, value): Sets the value of the rectangle
    height (self):Gets the height of the rectangle
    height (self, value):Sets the value of the rectangle
    area(self): Calculates the area ofthe rectangle
    perimeter(self):Finds the perimeter of the rectangle
    __str__(self): Returns a string representation of the rectangle
    __repr__(self): Returns a string representation of the rectangle
    suitable for debugging
    """


class Rectangle:
    """Class representing Rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initializes new rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle.
        Args:
            value (int): The new width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        Returns:
            int: Height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the new height  of the rectangle.
        Returns:
            int: height of the rectangle
        Raises:
            TypeError:if height not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self._height = value

    def area(self):
        """
        Calculates the erea of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            int: Perimeter of the triangle.
        """
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """
        Return string representation of the rectangle.
        Returns:
            str: Astring representation of ghe rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return (('#' * self._width + "\n")*self._height)[:-1]

    def __repr__(self):
        """
        Returns a string representation of rectangle suitable  for debugging
        Returns:
            str: Astring representation of the rectangle.
        """
        return 'Rectangle ({},{})'.format(self._width, self._height)
