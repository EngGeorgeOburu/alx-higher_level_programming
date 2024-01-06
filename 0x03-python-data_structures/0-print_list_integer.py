#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for int in my_list:
        # Using str.format() to print integers
        print("{:d}".format(int))
