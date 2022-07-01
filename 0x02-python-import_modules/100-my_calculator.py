#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    total = 0
    operators = ['+', '-', '*', '/']
    args = len(argv) - 1

    if args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if argv[2] == '+':
        a, b = int(argv[1]), int(argv[3])
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        a, b = int(argv[1]), int(argv[3])
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        a, b = int(argv[1]), int(argv[3])
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        a, b = int(argv[1]), int(argv[3])
        print("{} / {} = {}".format(a, b, div(a, b)))
