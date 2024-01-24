#!/usr/bin/python3

""" Define a class representing a square """


class Square:
    """ Initialize an instance of a class.
        parameter:
            size (int): Size of the circle.
        Raises:
            TypeError: Size must be an integer.
            ValueErro: size must be greatr than = 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
