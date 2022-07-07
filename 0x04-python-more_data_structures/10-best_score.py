#!/usr/bin/python3
def best_score(a_dictionary):
    """
    A function that returns a key with biggest integer value.

    Args:
        a_dictionary: The dictionary to be used.

    Return:
        A key with the largest value.
    """
    if not a_dictionary.values():
        return None
    return max(list(a_dictionary.values()))
