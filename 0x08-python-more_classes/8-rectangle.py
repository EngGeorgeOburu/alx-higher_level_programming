#!/usr/bin/python3
"""
This module define the class rectangle
Attributes:
    number_of_instances (int): Class variable to keep track of the
    instances created
    print_symbol(str):Class variable to define symbol used for printing
Methods:
    __init__(self, width=0, height=0):Initializes a new rectangle instance
    width(self):Gets thw width of the rectangle
    width(self, value):Gets the height of the rectangle
    height(self):Gets the height of the rectangle
    height(self, value):Sets the height of the rectangle
    area(self):Calculates the area of the rectangle
    perimeter(self):Calculates the perimeter of the rectangle.
    __str__(self):Returns sring representation of the rectangle
    __repr__(self):Decreases the number of instances when the rectangle
    is deleted
    bigger_or_equl(rect_1, rect_2):Compares 2 rectangles and return
    the largest on or egual to.
"""


class Rectangle:
    """
    Class Representing the rectangle.
    Attributes:
        number_of_instances:The number of instances of rectangle created
        print_symbol: The symbol used to print the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize new rectangle instance
        Args:
            width: Widht of the rectangle
            height:height of the rectangle
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle
        Returns:
            int: width of the rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the new width of the rectangle
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
            int: height
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the new height of the rectangle
        return:
            int: New height
        Raises:
            TypeError:if height not an integer
            ValueError: If height less than zero.
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
        int : area
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter ofthe rectangle
        Returns:
            int: Perimeter
        """
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str : string rep ofthe rectangle
        """
        if self._width == 0 or self._heigh == 0:
            return ""
        sys = str(self.print_symbol)
        return ((sys*self._width + "\n")*self._width)

    def __repr__(self):
        """
        Decreases the number of instances when reactgnle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("By rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the 2 reactangles based on their areas and return
        the larger one or equal one.
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Returns:
            Rectangle:The larger or equal rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of a rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of a rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2
        print("Bye rectangle...")
    
#    del __del__(self):
        #"""
       # Prints a message for each deletion.
        #"""
        #type(self).number_of_instance -= 1
        #printprint("Bye rectangle...")
