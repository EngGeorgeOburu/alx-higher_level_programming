#!/usr/bin/python3
""" Function that prints x elements of a list """


def safe_print_integer(value):
    """ Try to execute the following blockof code """
    try:
        """ Print the formatted interger value """
        print("{:d}".format(value))
        return True
    """ Handle the ValueError exception """
    except ValueError:
        return False
