#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        # Create a new list if Nothing is provided
        my_list = []
    for num in reversed(my_list):
        print("{:d}".format(num))
