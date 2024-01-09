#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list os empty
    if not my_list:
        return (None)
    # Initialize the max num with the first element
    max_num = my_list[0]
    # Iterate through the list finding max num
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
