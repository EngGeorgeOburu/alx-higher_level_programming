#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    """ Initialize these  sum of key and weight to 0 """
    sum_score = 0
    sum_weight = 0
    """ Iterate through each tuple in a list """
    for score, weight in my_list:
        """ Accumulate scores and weights """
        sum_score += score * weight
        sum_weight += weight
    """ Check if weight is not 0"""
    if sum_weight != 0:
        return sum_score / sum_weight
    else:
        return 0
