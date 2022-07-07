#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    A function that adds all unique integers in a list
    list.

    Args:
        my_list: The initial list

    Return:
        The sum of unique elements.
    """
    unique_list = set(my_list)
    return sum(unique_list)
