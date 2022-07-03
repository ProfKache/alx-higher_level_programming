#!/usr/bin/python3
def no_c(my_string):
    """
    The function that removes all characters c and C from a string.

    Args:
    my_string: The string containing the characters to be removed.
    """
    no_c_string = ''
    for character in my_string:
        if character.lower() != 'c':
            no_c_string += character

    return no_c_string
