#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        self._width=width
        self._height=height
        Rectangle.number_of_instances +=1
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._height=value
    def area(self):
        return self._width * self._height
    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)
    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        sys = str(self.print_symbol)
        return ((sys* self._width + "\n")*self.height)[:-1]
    def __repr__(self):
        return 'Rectangle {}, {}'.format(self._width, self._height)
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
