#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of attributes and methods of an object
    Args:
        obj (object): The object to inspect.
    Returns:
        List: A list containing the names of attributes and methods.
    """
    return [attr for attr in dir(obj)]
