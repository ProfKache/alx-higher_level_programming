#!/usr/bin/python3
"""
A program that imports the function def add(a, b): from the file add_0.py and
prints the result of the addition 1 + 2 = 3
Author: Salim J. Kachemela <sakachemela@gmail.com>
Date: Copyright (c) 2022.
"""
if __name__ == '__main__':
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
