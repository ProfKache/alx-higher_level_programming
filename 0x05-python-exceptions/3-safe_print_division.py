#!/usr/bin/python3
def safe_print_division(a, b):
    """
    A function divides 2 integers and prints the result.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print('Inside Result: {}'.format(result))
    return result
