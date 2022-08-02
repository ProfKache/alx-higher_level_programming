#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    A function prints x elements of a list.

    Args:
        my_list: a list that contains the items.
        x: the number of elements to print.
    """
    try:
        my_list_sliced = my_list[:x]
        for i in my_list_sliced:
            print(i, end='')
        print()
    except IndexError:
        print('Index Out of range')
    except TypeError:
        print('Unsupported Operation')
