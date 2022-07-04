#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    The function that finds the biggest integer of a list.

    Args:
        my_list: The list of integers.
    """
    if not my_list:
        return None
    # Assume the first number is the largest
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
