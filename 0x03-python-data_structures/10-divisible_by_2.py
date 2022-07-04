#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    The function that finds all multiples of 2 in a list.

    Args:
        my_list: The list of integers.
    """
    return [True if number % 2 == 0 else False for number in my_list]
