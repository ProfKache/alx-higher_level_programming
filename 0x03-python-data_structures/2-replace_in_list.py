#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    This function replaces an element of a list at a specific position like
    in C.

    Args:
        my_list: The list containing integers to be printed
        idx: The index to which the element is to be located.
        element: The actual replacement value.
    """
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
