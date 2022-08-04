#!/usr/bin/python3
"""
Program: 1-square.py
A program that demonstrates the use of Python classes
Author: Salim J. Kachemela <sakachemela@gmail.com>
Copyright (c) 2022
"""


class Square:
    """A class that defines a square with some instance attributes."""

    def __init__(self, size) -> None:
        """
        A constructor that initializes the size of the circle.

        Args:
            size(any): The size of the circle which is not specific.
        """
        self.__size = size
