#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    The function that prints a matrix of integers.

    Args:
        matrix: The matrix to be printed.
    """
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column < len(matrix[row]) - 1:
                print('{:d}'.format(matrix[row][column]), end=" ")
            else:
                print('{:d}'.format(matrix[row][column]), end="")
        print("")
