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
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print('Inside Result: {}'.format(result))
    return (result)
