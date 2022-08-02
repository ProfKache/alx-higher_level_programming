#!/usr/bin/python3
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
    except Exception as e:
        print('Exception:', e)
        return False
