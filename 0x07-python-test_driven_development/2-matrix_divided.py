#!/usr/bin/python3
"""  Divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.
    
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the\
        matrix elements by.
    
    Returns:
        list of lists: The new matrix with new elements  
    Raises:
        TypeError: If `matrix` is not a list of lists of\
        integers or floats, or if `div` is not a number.
        TypeError: If each row of the matrix does not\
        have the same size.
        ZeroDivisionError: If `div` is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) if isinstance(element, (int, float)) \
                   else element for element in row] for row in matrix]
    return new_matrix
