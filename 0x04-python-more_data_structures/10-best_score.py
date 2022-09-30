#!/usr/bin/python3

def best_score(a_dict):
    """
    a function that returns a key with the biggest integer value
    """
    if a_dict is None or a_dict == {}:
        return None
    for key in a_dict.keys():
        if a_dict[key] == max(a_dict.values()):
            return key
