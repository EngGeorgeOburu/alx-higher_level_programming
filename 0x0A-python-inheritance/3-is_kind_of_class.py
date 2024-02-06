#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    checks if an object can be inherited from a specified class
    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.
    Returns:
        bool: True if obj is an instance derived from the a_class,
        else False.
    """
    return isinstance(obj, a_class)
