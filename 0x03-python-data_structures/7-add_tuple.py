#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    The function that adds 2 tuples.

    Args:
        tuple_a: The first tuple
        tuple_b: The second tuple
    """
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_a) < 2 or len(tuple_b) < 2:
        if not len(tuple_a):
            tuple_a = 0, 0
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif not len(tuple_b):
            tuple_b = 0, 0
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif tuple_a[0] and len(tuple_a) == 1:
            tuple_a = tuple_a[0], 0
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif tuple_b[0] and len(tuple_b) == 1:
            tuple_b = tuple_b[0], 0
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
