#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instanceof the specified class.
    Args:
        obj (Object): The object to check
        a_class (class): The class to check against.
    Returns:
        bool:True if obj is exactly an instance of a_class,else False
    """
    return type(obj) is a_class
