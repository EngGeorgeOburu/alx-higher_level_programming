#!/usr/bin/python3
"""
This module saves an Object to a text file,using JSON rep
"""


def save_to_json_file(my_obj, filename):
    """
    Functions uses JSON representation to save object to text file.
    Args:
        my_obj (object): Object to be serialized.
        filename (str): The name of the file to write to.
    """
    import json
    with open(filename, mode='w', encoding='UTF8') as file:
        json.dump(my_obj, file)
