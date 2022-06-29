#!/usr/bin/python3
for number in range(0, 100):
    if len(str(number)) == 1:
        print(f"0{number}", end=', ')
    elif number > 9 and number <= 98:
        print(f"{number}", end=', ')
    else:
        print(f"{number}")
