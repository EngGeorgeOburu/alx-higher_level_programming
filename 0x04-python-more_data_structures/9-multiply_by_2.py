#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ Function that reurn new dictionary with all values x2 """
    mult_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return (mult_dict)
