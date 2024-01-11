#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    
    values = list(a_dictionary.keys())[0]
    max_value = a_dictionary[values]
    for i, j in a_dictionary.items():
        if j > max_value:
            max_value = j
            values = i
    return (values)
