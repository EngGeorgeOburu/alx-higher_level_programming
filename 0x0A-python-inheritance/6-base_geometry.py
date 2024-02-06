#!/usr/bin/python3
"""
This module defines a class with BaseGeometry properties.
"""


class BaseGeometry:
    """
    Base class
    """
    def area(self):
        """
        Raises an exception of area is not implemented
        """
        raise Exception("area() is not implemented")
