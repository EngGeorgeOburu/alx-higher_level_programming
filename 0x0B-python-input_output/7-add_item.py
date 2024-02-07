#!/usr/bin/python3
"""
This module provide a sript that adds all arguments to a python list.
"""


import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if not path.exists("add_item.json"):
    my_list = []
else:
    my_list = load_from_json_file("add_item.json")

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "and_item.json")

