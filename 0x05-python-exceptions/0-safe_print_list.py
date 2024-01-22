#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Initialize a counter for no. of elements to print"""
    elements_t0_print = 0
    try:
        """ Iterate through the first element of x in the list """
        for i in range(x):
            print(my_list[i], end="")
            elements_to_print += 1
        except IndexError:
        """ Handle the case when index is out of range """
        pass
    print()
    return elements_to_print
