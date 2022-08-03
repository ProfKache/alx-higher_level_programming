#!/usr/bin/python3
def magic_calculation(a, b):
    """
    A function that creates the application code to be equivalent to the
    bytecode.

    Args:
        a: the first parameter
        b: the second parameter
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
