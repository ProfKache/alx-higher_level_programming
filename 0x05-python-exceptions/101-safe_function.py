#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    A function executes a function safely.

    Args:
        fct: a reference to a function i.e a function pointer
        args: arbitrary number of arguments
    Return:
        The result of the function.
    """
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError):
        print('Exception: {}'.format(sys.exc_info()[1]), file=sys.stderr)
        return None
