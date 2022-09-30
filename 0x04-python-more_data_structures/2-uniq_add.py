#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    sum all unique integers in a list (only once for each integer
    """
    if my_list is None:
        return None
    return sum(set(my_list))
