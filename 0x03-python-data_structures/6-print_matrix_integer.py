#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    The function that prints a matrix of integers.

    Args:
        matrix: The matrix to be printed.
    """
    if matrix:
        for row in matrix:
            print(''.format(*row))
