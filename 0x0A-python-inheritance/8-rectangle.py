#!/usr/bin/python3

class BaseGeometry:
    """ Base class representing geometrical operations."""
    def area(self):
        """Raises an exception if area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value
        Args:
            name (str):Value name being validated.
            value (int): Value to be validated.
        Raises:
            TypeError: If value ! an integer
            ValueError: If Value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be an integer".format(name))


class Rectangle(BaseGeometry):
    """
    Class rep rectangle.
    Attributes:
        width (int): The width of the rectangle.
        height (int): Height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle
        Args:
            width (int) The width of the rectangle
            height  (int): The height of the rectangle.
        Raises:
            TypeError: If the width or height is not aninteger.
            ValueError: If the width or height is less than 0
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
