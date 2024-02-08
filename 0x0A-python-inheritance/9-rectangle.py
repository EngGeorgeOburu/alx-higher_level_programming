#!/usr/bin/python3
"""
Module: 9-rectangle

This module defines classes for representing geametric shapes.

Classes:
    BaseGeometry: Base class for geometry-related classes.
    Rectangle: Class representing a rectangle.
"""


class BaseGeometry:
    """
    Base class for geometry-related classes
    Methods:
        area(self): Raises an exception sinces its not implement
        integer_validator(self, name, value): Validates if the given
        value is an integer and greater than 0
    """

    def area(self):
        """
        Calculates the area of the geometry shape
        Raises:
            Exeception: Indicating that the method is not impelement.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value isan  integer and greater than 0
        if not isinstance(value, int):
        Args:
            name (str): The name of the value being validated
            value (int): The value to be validated.
        Raises:
            TypeError: If value not integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    Methods:
        area(self): Calculates the area of the rectangle
        __str__(self): Return a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initiliaze a rectangle with given height and width
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = 0
        self.__height = 0
        super().__integer_validator("width", width)
        super().__integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: Area of the rectangle
        """

        return self.__width * self.__height

    def __str__():
        """
        String representation of the rectangle
        Returns:
            str: String representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
