#!/usr/bin/python3
"""
A Program that prints the ASCII alphabet, in reverse order, alternating
lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by
a new line.
Author: Salim J. Kachemela <sakachemela@gmail.com>
Date: Copyright (c) 2022.
"""
for letter in range(122, 96, -1):
    if letter % 2 != 0:
        print("{}".format(chr(letter).upper()), end='')
    else:
        print("{}".format(chr(letter)), end='')
