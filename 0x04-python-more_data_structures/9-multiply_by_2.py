#!/usr/bin/python3

def multiply_by_2(a_dict):
    """
    a function that returns a new dictionary with all values multiplied by 2
    """
    if a_dict is None:
        return None
    else:
        return {key: a_dict[key] * 2 for key in a_dict}
