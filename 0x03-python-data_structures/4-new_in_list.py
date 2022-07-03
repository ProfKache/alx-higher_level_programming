#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    A function replaces an element in a list at a specific position without
    modifying the original list (like in C).

    Args:
        my_list: The list containing integers to be printed.
        idx: The index/position of the element to be replaced.
        element: The element to replace with.
    """
    if idx < 0:
        return my_list[:]
    elif idx > (len(my_list) - 1):
        return my_list[:]
    else:
        my_list_copy = my_list[:]
        my_list_copy[idx] = element
        return my_list_copy
