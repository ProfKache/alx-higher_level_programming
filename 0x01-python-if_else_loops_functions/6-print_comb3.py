#!/usr/bin/python3
for number in range(0, 100):
    first_number = number / 10
    second_number = number % 10

    if first_number < second_number and first_number != second_number and \
            number != 89:
        print("{:02d}, ".format(number), end='')
    if number == 89:
        print("{}".format(number))
