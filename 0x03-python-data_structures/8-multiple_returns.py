#!/usr/bin/python3
def multiple_returns(sentence):
    """
    The function that returns a tuple with the length of a string and its first
    character.

    Args:
        sentence: The string to be evaluated against.
    """
    return (int(len(sentence)), sentence[0])
