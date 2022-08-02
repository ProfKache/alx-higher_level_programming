#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    A function that prints an integer with error message

    Args:
        value (int/str): A value to be printed
    Return:
        True if value is an integer, otherwise return False if an exception
        occurs, together with a stderr
    """
    try:
        print('{:d}'.format(value))
        return True
    except (TypeError, ValueError):
        print('Exception: {}'.format(sys.exc_info()[1]), file=sys.stderr)
        return False
