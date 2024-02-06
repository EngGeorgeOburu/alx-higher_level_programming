#!/usr/bin/python3

class BaseGeometry:
    """
    Base class
    """
    def area(self):
        """
        Raises an exception of area is not implemented
        """
        raise Exception("area() is not implemented")
