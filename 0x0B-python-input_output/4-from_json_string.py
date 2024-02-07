#!/usr/bin/python3
"""
This module returns an objct  represented by a JSON string.
"""


def from_json_string(my_str):
    """
    Function returning  an object
    Args:
        my_str (str): The JSON string to parse.
    Returns:
        object: The python data structures representedjson string.
    """
    import json
    return json.loads(my_str)
