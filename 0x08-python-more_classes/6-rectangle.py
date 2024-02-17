#!/usr/bin/python3
"""
This module definesa rectangle class.
Attributes:
    -width (int): Width of the rectangle
    -height (int): Height of the rectangle
    number_of_instances (int):The count of instances of the rectangle class
Methods:
    __init__(self, width=0, height=0): Initialize a new rectangle instances
    width(self):Gets the width of the rectangle.
    width(self, value):Sets the new width of the rectangle.
    height(self): Gets the height of the rectangle.
    height(self, value): Sets the new height of the rectangle.
    area(self):Calculates the area of the rectangle
    perimeter(self):Calculates the perimeter of the rectangle.
    __str__(self): Returns a string representation of the rectangle.
    __repr__(self): Returns a string representation of the rectangle
        suitanlefor debugging.
    __del__(self): Destructor for cleaning up resources.
"""


class Rectangle:
    """
    Class representing a Rectangle.
    Attributes:
        number_of_instances: Keep track of no.of instances created.

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self._width = width
        self._heigth = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle
        Returns:
            int: width
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle.
        Returns:
            int: New width
        Raises:
            TypeError: If width not an integer
            ValueError: If width is less than 0
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
            int:Heigt
        """
        return self._width

    @height.setter
    def height(self, value):
        """
        Sets the new height of the rectangle
        Returns:
            int: New height
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            int:Area
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            int: Perimeter
        """
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """
        String representation for the rectangle.
        Returns:
            str: String represention of the rectangle
        """
        return (('#' + self._width + "\n")*self._height)[:-1]

    def __repr__(self):
        """
        String representation making it suitable for debugging
        Returns:
            str: string rep of rectangle
        """
        return 'Rectangle {}, {}'.format(self._width, self._height)

    def __del__(self):
        """
        Desstructor for cleaning up resources.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
