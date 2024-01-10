#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Calculate the square value of all integers in a matrix"""
    return [[element ** 2 for element in row] for row in matrix]
