#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences of an element by another in a new
    list.

    Args:
        my_list: The initial list
        search: The element to replace in the list
        replace: The new element

    Return:
        A new list with some elements replaced.
    """
    new_list = my_list[:]
    for number in new_list:
        if number == search:
            index = new_list.index(number)
            new_list[index] = replace

    return new_list
