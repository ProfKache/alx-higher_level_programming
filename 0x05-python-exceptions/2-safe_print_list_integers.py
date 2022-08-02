#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    A function prints x elements of a list.

    Args:
        my_list: a list that contains the items.
        x: the number of elements to print.
    Return:
        The number elements to be printed.
    """
    i = 0
    for i in range(0, x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            i += 1
        except (ValueError, TypeError):
            continue
    print("")
    return i
