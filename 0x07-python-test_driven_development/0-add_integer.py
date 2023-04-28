#!/usr/bin/python3
"""
Program: 0-add_integer.py
A program that demonstrates TDD in Python
Author: Salim J. Kachemela <sakachemela@gmail.com>
Copyright (c) 2023
"""


def add_integer(a: int, b: int = 98) -> int:
    """
    This function adds two integers

    Args:
        a(int): The first number or operand.
        b(int): The second number of operand.

    Return:
        An integer i.e the addition of a and b
    """
    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
