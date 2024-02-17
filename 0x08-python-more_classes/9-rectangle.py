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

    def __init__(self, width=0
