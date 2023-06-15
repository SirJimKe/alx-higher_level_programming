#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix"""
    result = [[0 for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    return result
