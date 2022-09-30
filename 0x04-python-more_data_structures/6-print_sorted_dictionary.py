#!/usr/bin/python3

def print_sorted_dictionary(a_dict):
    """
    print a dict in sorted order of keys
    """
    if a_dict is None:
        return None
    for key in sorted(a_dict.keys()):
        print("{:s}: {}".format(key, a_dict[key]))
