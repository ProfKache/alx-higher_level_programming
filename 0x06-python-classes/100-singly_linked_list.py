#!/usr/bin/python3
"""
Program: 100-singly_linked_list.py.py
A program that demonstratesa single linked list.
Author: Salim J. Kachemela <sakachemela@gmail.com>
Copyright (c) 2022
"""


class Node:
    """A class that defines that defines a node of a singly linked list."""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        A constructor that initializes the size of the circle.

        Args:
            size(int): The size of the circle
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the circle to be returned."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """ Return the circle position """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(x, int) for x in value) or\
                not all(n >= 0 for n in value):
            raise TypeError('position must be a tuple of 2 positive intergers')
        self.__position = value

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
            return

        [print("") for _ in range(0, self.position[1])]
        for _ in range(self.size):
            [print(" ", end="") for _ in range(0, self.position[0])]
            [print("#", end="") for _ in range(0, self.size)]
            print("")