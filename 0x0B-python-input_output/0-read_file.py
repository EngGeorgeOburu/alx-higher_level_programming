#!/usr/bin/python3
"""
This module reads a text file and prints it to the stdoup
"""


def read_file(filename=""):
    """
    Function reads text file UTF8 and prints to the stdout
    Args:
       filename ( str): The file name to be read.
    """
    with open(filename, encoding='UTF8') as file:
        for line in file:
            print(line, end='')
