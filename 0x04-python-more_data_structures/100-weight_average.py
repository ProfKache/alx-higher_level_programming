#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    A function that returns the weighted average of all integers
    tuple (<score> , <weight>)

    Args:
        my_list: a list of all integers

    Return:
        the weighted average of all integers tuple
    """
    if len(my_list) == 0:
        return 0
    return sum([(x[0] * x[1]) for x in my_list]) / sum([x[1] for x in my_list])
