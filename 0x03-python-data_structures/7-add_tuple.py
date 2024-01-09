#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Check if the length of tuple_a is >= 2
    if len(tuple_a) >= 2:
        a1, a2 = tuple_a[:2]  # Extract the first two elements
    else:
        a1, a2 = 0, 0  # Default values if the length is < 2
    # Check if the lenghth of tuple_b is >= 2
    if len(tuple_b) >= 2:
        b1, b2 = tuple_b[:2]  # Extract the first two elements
    else:
        b1, b2 = 0, 0  # Default values if the length is < 2
    # Return the results of the corresponding elements
    return (a1 + b1, a2 + b2)
