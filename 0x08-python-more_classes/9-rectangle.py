#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """
    Class representing a rectangle
    Attributes:
        number_of_instances: Number of instances of rectangle created.
        print_symbol: The symbol used to print the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the new rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the new width of the new rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the new rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height be >= 0")
        self.__height = value

    def area(self):
        """
        Defines the area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Defines the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checks which rectangleis greater than the other.
        Args:
            rect_1: The first rectangle
            rect_2: The second rectangle
        Raises:
            TypeError:If rect_1 or rect_2 is not a triangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of a rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of a rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """
        Returns the printable representation of the rectangle.
        Represents the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        Returns the string representation of the Rectangle.
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """
        Prints a message for every deletion.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
