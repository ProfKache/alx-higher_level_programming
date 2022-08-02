#!/usr/bin/python3
def safe_print_integer(value):
    """
    A function that prints an integer with "{:d}".format().

    Args:
        value (int): A value to be printed
    Return:
        True if value is an integer, otherwise return False if an exception
        occurs
    """
    try:
        print('{:d}'.format(value))
        return True
    except (ValueError, TypeError):
        return False
