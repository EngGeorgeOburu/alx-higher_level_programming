#!/usr/bin/python3
"""
A class representing a square
Attributes:
    __size (int): Size of the square
Methods:
    __init__(self, int): Initializes a new square instance
    size(self): Getter method for retreiving size of the square
    size(self, value): Setter method for setting size of the square
    area(self): Calculates the area of the square
    my_print(self): Print the visual representation of the square \
            using '#' character
"""


class Square:
    """
    Initializez a new square instance
    parameter:
    size (int): Size of the square
    raises:
    TypeError: if size not integer
    ValueError: if size is less than 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError(" size must be >= 0")
        self.__size = size
    """
    Getter method for retriving size of the square
    int: size of square
    """
    @property
    def size(self):
        return self.__size
    """
    Setter method for setting size of the square
    Raises:
    TypeError: If size is not an interger
    ValueError: If size is less than 0
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0 ")
        self.__size = value
    """
    Calculates the area of the square
    Returns:
    int: Area of the square
    """
    def area(self):
        return self.__size ** 2
    """
    Prints the visual representation of the square using '#' character
    """
    def my_print(self):
        if self.size == 0:
            print()
            return None
        for i in range(1, self.area() + 1):
            print('#', end='')
            if (i % self.__size == 0 and i >= 0):
                print()
