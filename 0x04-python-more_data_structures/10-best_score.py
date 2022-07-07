#!/usr/bin/python3
def best_score(a_dictionary):
    """
    A function that returns a key with biggest integer value.

    Args:
        a_dictionary: The dictionary to be used.

    Return:
        A key with the largest value.
    """
    if not a_dictionary:
        return None
    highest_score = max(list(a_dictionary.values()))
    for name, marks in a_dictionary.items():
        if marks == highest_score:
            return name
