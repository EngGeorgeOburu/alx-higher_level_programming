#!/usr/bin/python3
""" Function that prints the 1st x elements of a list and only intergers """


def safe_print_list_integers(my_list=[], x=0):
    """ Initialize the counter for the printed elements """
    printed_element = 0
    """ Iterate through the range of minimum of x and the length of my_list """
    for i in range(0, min(x, len(my_list))):
        try:
            """ Print the current element as an interger """
            print("{:d}".format(my_list[i]), end="")
            """ Increment the counter for printed element """
            printed_element += 1
        """ Handle ValueError or TypeError as exceptions """
        except (ValueError, TypeError):
            """ Continues to the next iteration if an exception occurs """
            continue
    """ Print a new line after printing the elements """
    print()
    return printed_element
