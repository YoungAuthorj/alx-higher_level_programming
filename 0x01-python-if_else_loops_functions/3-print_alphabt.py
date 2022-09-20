#!/usr/bin/python3
for i in range(ord("a"), ord("z") + 1):
    if chr(i) == "q" or chr(i) == "e":
        continue
    else:
        print("{:s}".format(chr(i)), end="")
