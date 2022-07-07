#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    A function that adds all unique integers in a list
    list.

    Args:
        my_list: The initial list

    Return:
        A new list with some elements replaced.
    """
    unique_list = set(my_list)
    return sum(unique_list)
