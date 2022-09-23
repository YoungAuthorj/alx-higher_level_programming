#!/usr/bin/python3
import hidden_4 as h


def discover():
    name = dir(h)
    for i in name:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    discover()
