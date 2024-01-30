#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self._width=width
        self._height=height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.height=value
    def area(self):
        return self._width * self._height
    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)
    def __str__(self):
        if self._width == 0 or self._heigh == 0:
            return ""
        sys = str(self.print_symbol)
        return ((sys*self._width + "\n")*self._width)
    def __repr__(self):
        Rectangle.number_of_instances -= 1
        print("By rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of a rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of a rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2
