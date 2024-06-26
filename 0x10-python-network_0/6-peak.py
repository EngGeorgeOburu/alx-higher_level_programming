#!/usr/bin/python3
""" Peak finding algorithm."""


def find_peak(list_of_integers):
    """
    Returns a peak in a list in the unsorted integers.
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    midd = int(size/2)
    peak = list_of_integers[midd]
    if peak > list_of_integers[midd - 1] and peak > list_of_integers[midd + 1]:
        return peak
    elif peak < list_of_integers[midd - 1]:
        return find_peaj(list_of_intgers[:midd])
    else:
        return find_peak(list_of_integers[midd + 1:])
