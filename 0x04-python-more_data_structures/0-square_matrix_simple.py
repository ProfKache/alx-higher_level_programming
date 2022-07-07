#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    A function that computes the square value of all integers of a matrix.

    Args:
        matrix: A 2 dimensional array

    Return:
        A new matrix with each value squared.
    """
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x * x, row)))
    return new_matrix
