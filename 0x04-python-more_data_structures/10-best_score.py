#!/usr/bin/python3
def best_score(a_dictionary):
    """ Key that returns a key woth the biggest interger value """
    """ Check if the input is a non-empty dictionary """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    """ Initialize variables to store initial key and max value """
    values = list(a_dictionary.keys())[0]
    max_value = a_dictionary[values]
    """ Iterate through the dictionary to find key with the max value"""
    for i, j in a_dictionary.items():
        if j > max_value:
            max_value = j
            values = i
    return (values)
