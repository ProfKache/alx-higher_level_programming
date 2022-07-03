#!/usr/bin/python3
"""
A program that prints Python bytecode
Author: Salim J. Kachemela <sakachemela@gmail.com>
Date: Copyright (c) 2022.
"""


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c

    return sub(a, b)
