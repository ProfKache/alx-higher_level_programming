#!/usr/bin/python3
def safe_print_division(a, b):
    """
    A function divides 2 integers and prints the result.

    Args:
        a: the first integer
        b: the second integer
    Return:
        The result of division of a and b
    """
    result = None
    try:
        result = a / b
        return result
    except (ZeroDivisionError, ValueError, TypeError, FloatingPointError):
        return None
    finally:
        print('Inside Result: {}'.format(result))
