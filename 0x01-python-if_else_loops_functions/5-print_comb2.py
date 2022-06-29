#!/usr/bin/python3
for number in range(0, 100):
    if len(str(number)) == 1:
        print("0{}".format(number), end=', ')
    elif number > 9 and number <= 98:
        print("{}".format(number), end=', ')
    else:
        print("{}".format(number))
