#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides element by element 2 lists.

    Args:
        my_list_1 (list): the first list
        my_list_2 (list): the second list
        list_length (int): the number of elements to be divided
    Return:
        A new list of length list_length containing all the divisions.
    """
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
            result = 0
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        except IndexError:
            print('out of range')
            result = 0
        finally:
            result_list.append(result)
    return result_list
