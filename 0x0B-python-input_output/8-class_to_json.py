#!/usr/bin/python3
"""
This module provides a function that returns the dictionary description with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return the dictionary with simple data structures for JSON
    serialization of an object
    Args:
        obj: An instance of a class.
    Returns:
        dict: A dictionary description of the object suitable forJSON serialization.
    """

    """ Get all the attributes of the object."""
    attributes = obj.__dict__

    """ Convert any non serializable attributes to serializable form"""
    for key, value in attribute.items():
        """If the attribute is not a basic dat type, convert it ti its JSON-serializable form."""
        if not isinstance(value, (list, dict, str, int, bool)):
            attributes[key] = str(value)
        return attributes
