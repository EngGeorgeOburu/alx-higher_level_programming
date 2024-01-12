#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ Functions that deletes a key in dictionary """
    """ Check if key exits in dictionary """
    if key in a_dictionary:
        """ If yes, delete it from the dictionary"""
        del a_dictionary[key]
    return (a_dictionary)
