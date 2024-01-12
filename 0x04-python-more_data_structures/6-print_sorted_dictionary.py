#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Function that prints a dictionary by ordered keys """
    """ Iterate through keys in the dictionary """
    for key in sorted(a_dictionary):
        """ Print each key-value pair """
        print("{}: {}".format(key, a_dictionary[key]))
