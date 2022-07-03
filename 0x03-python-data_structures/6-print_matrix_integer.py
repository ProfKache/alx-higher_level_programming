#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    The function that prints a matrix of integers.

    Args:
        matrix: The matrix to be printed.
    """
    for row in matrix:
        if row:
            print('{:d} {:d} {:d}'.format(*row))
        print('')
