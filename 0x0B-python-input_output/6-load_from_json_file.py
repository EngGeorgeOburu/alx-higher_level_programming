#!/usr/bin/python3
"""
This module provides afunction that creates an Object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Functions creates an object from a JSON file.
    Args:
        filename (str): Name of the JSON file to read from.
    Returns:
        Object: The python data structure represented by the JSON file
    """
    def load_from_json_file(filename):
        with open(filename, mode='r', encoding='UTF8') as file:
            return json.load(file)
