#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    The function that prints a matrix of integers.

    Args:
        matrix: The matrix to be printed.
    """
    if len(matrix[0]):
        for row in matrix:
            for column in row:
                print('{}'.format(column), end=" ")
            print()
        print()
        # if row:
        # print('{:d} {:d} {:d}'.format(*row))
        # else:
        # print()
