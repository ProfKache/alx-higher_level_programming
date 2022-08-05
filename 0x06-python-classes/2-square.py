#!/usr/bin/python3
"""
Program: 2-square.py
A program that demonstrates the use of Python classes
Author: Salim J. Kachemela <sakachemela@gmail.com>
Copyright (c) 2022
"""


class Square:
    """A class that defines a square with some instance attributes."""

    def __init__(self, size=0) -> None:
        """
        A constructor that initializes the size of the circle.

        Args:
            size(int): The size of the circle
        """
        if not isinstance(size, int):
            print('size must be an integer')
        elif size < 0:
            print('size must be >= 0')
        self.__size = size
