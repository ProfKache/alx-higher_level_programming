#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    A function that returns the number of keysin a dictionary.

    Args:
        a_dictionary: The dictionary to be used to count with keys.

    Return:
        The total number of keys in a dictionary
    """
    keys = 0
    for _ in a_dictionary.keys():
        keys += 1

    return keys
