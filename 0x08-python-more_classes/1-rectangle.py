#!/usr/bin/python3
"""
This module defines a Rectangle class.
Attributes:
    -width (int): The width ofthe rectangle.
    -height (int): The height of the rectangle.

Methods:
    __init__(self, width=0, height=0):Initialize a new \
            rectangle with given height and width
    width(self): Gets the width of the rectangle.
    height(self, value): Sets the width of the rectangle.
    height(self): Gests the height of the rectangle.
    height(self, value):Sets the height of the rectangle.
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.
        Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle.

        Args:
            Value (int): The new width value.
        Raises:
            TypeError:If value not integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the triangle.

        Returns:
            int: The height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

            Raises:
            TypeErro: if velue is not integer.
            ValueError: if value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
