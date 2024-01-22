#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_element = 0
    for i in range(x):
        try:
            print("my_list[i], end="" ")
            printed_elements += 1
        except ValueError:
            continue
    print()
    return printed_element    
