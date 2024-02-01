#!/usr/bin/python3
"""
This module defines representation of rectangle class
Attributes:
    -width(int): Width of the rectangle
    -height(int):Height of the rectangle
Methods:
    __inti__(self, width=0, height=0):Initializes new rectangle instance.
    width(self):Gets the width of the rectangle
    width(self, value): Sets the width of the rectangle
    height(self): Gets the height of the rectangle
    height(self, value): Sets the height of the rectangle
    area(self): Calculates the area of the rectangle
    perimeter(self):Calculates the perimeter of the rectangle
    __str__(self):String representationof the rectangle
    __repr__(self):String representation of rectangle suitable for debugging
    __del__(self):Deconstrutor for cleaning up reseources

"""


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes new instance of rectangle
        Args:
            -width: Width of the rectangle
            -height: Height of the rectangle
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of rectangle
        Returns:
            int: Width
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle
        Returns:
            int: Width
        Raises:
            TypeError: if width not an integer
            ValueError: If width less than zero
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
            int: Height
        """
        return self._height

    @height.setter
    def height(self):
        """
        Sets the new height of the rectangle
        Returns:
            int: Height
        Raises:
            TypeError:If height is not an integer
            ValueError:If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            int: Area
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            int: Perimeter
        """
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """
        String representation of the rectangle
        Returns:
            str: Representation of rectangle
        """
        if self._width == 0 or self._height == 0:
            return ""
        sys = str(self.print_symbol)
        return ((sys * self._width + "\n") * self.height)[:-1]

    def __repr__(self):
        """
        String representation for the rectangle suitable for debugging
        Returns:
            str: String rep of rectangle
        """
        return 'Rectangle {}, {}'.format(self._width, self._height)

    def __del__(self):
        """
        Deconstructor Method for cleaning up process
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
