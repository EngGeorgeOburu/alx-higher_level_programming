#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.
    Args:
        matrix (list of lists): input matrix where inner list \
                represent a row
        div (int or float): The divisor.
    Returns:
    list of lists: A new matrix with elements rounded to 2 dp
    Raises:
    TypeError: if matrix is not list of lists of integers\
            or float, row different sizes
    ZeroDivisionError:If div is 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(element, (int, float))
            for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)of"
                "integers/float")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matric must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division be zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
