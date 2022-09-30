#!/usr/bin/python3

def simple_delete(a_dict, key=""):
    """
    a function that deletes a key in a dictionary
    """
    if a_dict is None:
        return None
    if key in a_dict:
        del a_dict[key]
    return a_dict
