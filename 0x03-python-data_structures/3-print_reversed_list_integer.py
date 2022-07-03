#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    This function prints all integers of a list, in reverse order.

    Args:
        my_list: The list containing integers to be printed in reverse.
    """
    for number in reversed(my_list):
        print('{:d}'.format(number))
