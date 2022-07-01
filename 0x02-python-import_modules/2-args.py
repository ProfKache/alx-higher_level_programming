#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    total_args = len(argv) - 1

    if total_args == 0:
        print(f'{total_args} arguments.')
    elif total_args == 1:
        print(f'{total_args} argument:')
        print(f"{total_args}: {argv[1]}")
    elif total_args > 1:
        print(f'{total_args} arguments:')
        for index, _ in enumerate(range(1, total_args + 1), start=1):
            print(f"{index}: {argv[index]}")
