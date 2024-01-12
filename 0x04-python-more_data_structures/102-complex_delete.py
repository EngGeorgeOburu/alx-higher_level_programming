#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Delete keys with specific values in the dictionary"""
    for _ in range(list(a_dictionary.values()).count(value)):
        for k, v in list(a_dictionary.items()):
            if v == value:
                del a_dictionary[k]
                break
    return a_dictionary
