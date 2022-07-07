#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    A function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The dictionary to be used.
        key: The key for the dictionary which always be a string.
        value: The dictionary value, which can be any type.

    Return:
        A dictionary with sorted keys.
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
