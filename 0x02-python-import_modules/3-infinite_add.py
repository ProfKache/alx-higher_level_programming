#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    total = 0
    args = len(argv) - 1

    if args <= 0:
        print(f'{total}')
    else:
        for arg in range(1, args + 1):
            total += int(argv[arg])
        print(f'{total}')
