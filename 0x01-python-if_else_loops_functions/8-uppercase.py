#!/usr/bin/python3
def uppercase(str):
    """
    Convert the string to uppercase followed by a new line.
    """
    for i in range(len(str)):
        upper = str[i]
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            upper = chr(ord(str[i]) - 32)
        print("{}".format(upper), end='')
    print()
