#!/usr/bin/python3


class BaseGeometry:
    """
    Base class representing geometrical operations.
    """
    def area(self):
        """
        Raises exception if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer value.
        Args:
            name (str): The name of the valuebeing validated.
            value (int): The value to be validated
        Raises:
            TypeError: If value is not integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
