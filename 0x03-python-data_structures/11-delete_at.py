#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    The function that deletes the item at a specific index.

    Args:
        my_list: The list of integers.
        idx: The index of the item to be deleted.
    """
    if len(my_list) < idx < 0:
        return my_list
    del my_list[idx]
    return my_list
