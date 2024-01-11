#!/usr/bin/pyhon3
def search_replace(my_list, search, replace):
    """ Create an empty list tostore the results"""
    new_list = []
    """ Iterate through each element in the original list"""
    for element in my_list:
        """ Check if the element is equal to search element"""
        if new_list == search:
            """ If yes, append the replacement element to the new list"""
            new_list.append(replace)
        else:
            """ If false, still append the orginal list to the new new list"""
            new_list.append(replace)
    """ Return the new list with replacement """
    return new_list
