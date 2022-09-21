#!/usr/bin/python3
i = 122
while i >= 97:
    move = 0
    if i % 2 != 0:
        i = i - 32
        move = 1
    print("{:s}".format(chr(i)), end="")
    if move == 1:
        i = i + 32
    i = i - 1
