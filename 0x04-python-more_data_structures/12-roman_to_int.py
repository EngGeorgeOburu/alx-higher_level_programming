#!/usr/bin/python3
def roman_to_int(roman_string):
    """ A function that converts roman numeral to an integer """
    """ Checkif the input is not empty string """
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    """ Dictionary to map roman numerals to interger """
    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    results = 0
    last_value = 0
    """ Iterate through reversed roman numeral string """
    for number in reversed(roman_string):
        """ Get the interger == to current roman numeral """
        value = roman_nums[number]
        """ Compare the current value with the prev one """
        if value < last_value:
            """ Substract the current value if it is < the previous one"""
            results -= value
        else:
            """ Add the current value if it >= to the previous one """
            results += value
        """ Update the next value for the next iteration """
        last_value = value
    return results
