#!/usr/bin/python3
"""Defines a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name.
    Args:
    first_name: first name
    last_name: last name
    Raises:
    TypeError: if name not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
