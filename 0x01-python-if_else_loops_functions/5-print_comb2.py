#!/usr/bin/python3
for number in range(0, 100):
    if number <= 98:
        print("{:02}".format(number), end=', ')
    else:
        print("{}".format(number))
