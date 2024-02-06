#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Checks if an instance of a class can be inherited
    Args:
        obj (objects): The object to check.
        a_class (class): The class to check against.
    Returns:
        bool:True if instance of a class can be inherted
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
