#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return (0,None)
    else:
        del my_list[idx]
        return (1, my_list)
