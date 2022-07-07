#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The dictionary to be used.
        key: The key for the dictionary which always be a string.
        value: The dictionary value, which can be any type.

    Return:
        A dictionary with sorted keys.
    """
    a_dictionary.update({key: value})

    return a_dictionary
