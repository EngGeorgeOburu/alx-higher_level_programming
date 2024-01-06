#!/usr/bin/python3
def element_at(my_list, idx):
 # Checks if the idx is negative or greater than the no. of elements in the list provided
  if idx < 0 or idx > len(my_list):
    return None
  return my_list[idx]
