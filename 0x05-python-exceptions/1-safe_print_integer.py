#!/usr/bin/python3
def safe_print_integer(value):
    """
    A function that prints an integer with "{:d}".format().

    Args:
        value: A value to be printed
    """
    try:
        print('{:d}'.format(value))
        print()
        return True
    except ValueError:
        print()
        return False
