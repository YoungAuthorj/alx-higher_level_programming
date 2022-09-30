#!/usr/bin/python3

def update_dictionary(a_dict, key, value):
    """
    add or replace a new key value in dict
    """
    if a_dict is None:
        return None
    a_dict[key] = value
    return a_dict
