#!/usr/bin/python3
"""
A Program that creates a copy of the string, removing the character at the
position n (not the Python way, the “C array index”).
Author: Salim J. Kachemela <sakachemela@gmail.com>
Date: Copyright (c) 2022.
"""


def remove_char_at(str, n):
    """
    A function that creates a copy of the string, removing the character at the
    position n (not the Python way, the “C array index”).
    """
    if len(str) <= n or n < 0:
        return str
    return str.replace(str[n], '')
