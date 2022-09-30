#!/usr/bin/python3

def number_keys(a_dict):
    """
    return the number of keys in a dict
    """
    if a_dict is None:
        return None
    return len(a_dict.keys())
