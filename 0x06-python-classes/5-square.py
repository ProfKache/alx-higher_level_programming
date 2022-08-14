#!/usr/bin/python3
"""
Program: 5-square.py
A program that demonstrates the use of Python classes and instance methods.
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
        self.size = size

    @property
    def size(self):
        """str: The size of the circle to be returned."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """ A method that calculates an area of a square
            Returns:
                The area of a square.
        """
        return self.size**2

    def my_print(self):
        """
        A method that prints the square to the stdout with character #.
        """
        if self.size == 0:
            print()
        for _ in range(self.size):
            print("#"*self.size)
