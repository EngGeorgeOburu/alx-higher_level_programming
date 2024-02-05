#!/usr/bin/python3

def lookup(obj):
    """ Returns the list of attributes and methods of an object """
    return [attr for attr in dir(obj)]
