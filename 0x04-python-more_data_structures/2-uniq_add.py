#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Function that adds the sum ofunique elements in a list"""
    """ Initialize sum variable to zero """
    sum = 0
    """ Iterate through the set of unique elements in the list """
    for i in set(my_list):
        sum += i
    return (sum)
