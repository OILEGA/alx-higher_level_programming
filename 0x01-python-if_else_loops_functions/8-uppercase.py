#!/usr/bin/python3

def uppercase(str):
    for alpha in str:
        if ord(alpha) >= 97 and ord(alpha) <= 122:
            alpha = chr(ord(alpha) - 32)
        print("{:s}".format(alpha), end='')
    print('\n', end="")
