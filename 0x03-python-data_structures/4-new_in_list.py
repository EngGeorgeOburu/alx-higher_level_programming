#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is out of range or negative
    if idx < 0 or idx >= len(my_list):
        # [:] is used to indicate start,end and step indices
        return my_list[:]  # Return a copy of the new element
    new_list = my_list[:]  # Creating a new list using list slicing
    new_list[idx] = element
    return new_list
