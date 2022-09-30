#!/usr/bin/python3

def complex_delete(a_dict, value):
    """
    removes a value in a dictiinary
    """
    if a_dict is None:
        return None
    delete_key = None
    keys = tuple(a_dict.keys())
    for key in keys:
        if a_dict[key] == value:
            del a_dict[key]
    return a_dict
