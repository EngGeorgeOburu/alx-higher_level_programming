#!/usr/bin/python3

class Rectangle:
    number_of_instances=0
    def __init__(self, width=0, height=0):
        self._width=width
        self._heigth=height
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
    @property
    def height(self):
        return self._width
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._height=value
    def area(self):
        return self._width * self._height
    def perimeter(self):
        return (self._width * 2) + (self._height * 2)
    def __str__(self):
        return (('#' + self._width + "\n")*self._height)[:-1]
    def __repr__(self):
        return 'Rectangle {}, {}'.format(self._width, self._height)
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
