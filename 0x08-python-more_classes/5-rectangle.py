#!/usr/bin/python3
"""
This module defines a rectangle class.
Attributes:
    -width (int): The width of the rectangle.
    -height (int): The height of the rectangle.
Methods:
    __init__(self, width=0, height=0): Initialize a new rectangle instance.
    width(self):Gets the width of the rectangle
    width(self, value): Sets the new width of the rectangle.
    height(self):Gets the height of the rectangle.
    height(self, value): Sets the new height of the rectangle
    area(self): Calculates the area of the rectangle.
    perimeter(self):Calculates the perimeter of the rectangle.
    __str__(self):Returns a string representation of the rectangle.
    __repr__(self):Returns a string representation of the rectangle
        suitable for debugging
    __del__(self):Destructor method for cleaning up resources
        (not implemented in the code).
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.
        Args:
            width (int): The width of the rectangle
            height (int): The height ofthe rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        Returns:
            int: width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle.
        Returns:
            int: new width of the rectangle.
        Raises:
            TypeError: If width is not integer.
            ValueError: If width is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        Returns:
        int: height
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the new height
        Returns:
            int: new height
        Raises:
            TypeError: If height not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            int: Area of the rectangle
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            int: Perimeter
        """
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: String rep of the rectangle
        """
        return (('#' * self._width + "\n") * self._height)[:-1]

    def __repr__(self):
        """
        Returns string rep of the rectangle suitable for debugging.
        Returns:
            str: String rep of the rectangle
        """
        return 'Rectangle {},{}'.format(self._width, self._height)

    def __del__(self):
        """
        Destructor method for cleaningresources.
        (Note: Not implemented in the provided code
        """
        print("Bye rectangle...")
