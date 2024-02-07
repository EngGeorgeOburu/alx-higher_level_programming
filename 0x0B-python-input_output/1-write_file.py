#!/usr/bin/python3
"""
This module writes a string to a text file and return the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file(UTF8)
    Args:
        filename (str): Name of the file to write to
        text (str): The tring to write to the file
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='UTF8') as file:
        return file.write(text)
