#!/usr/bin/python3
"""
This module appends a string at the end of a text file UTF8
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Functions append string at the end of the text file
    """
    with open(filename, mode='a', encoding='UTF8') as file:
        return file.write(text)
