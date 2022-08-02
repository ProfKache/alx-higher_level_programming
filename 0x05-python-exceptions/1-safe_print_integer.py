#!/usr/bin/python3
def safe_print_integer(value):
    """
    A function that prints an integer with "{:d}".format().

    Args:
        value: A value to be printed
    """
    if isinstance(value, int):
        return True
    try:
        print('{:d}'.format(value))
    except ValueError:
        return False
