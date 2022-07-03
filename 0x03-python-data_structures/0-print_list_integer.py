#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    This function prints all integers of a list.

    Args:
    my_list: The list containing integers to be printed
    """
    for number in my_list:
        print('{:d}'.format(number))
