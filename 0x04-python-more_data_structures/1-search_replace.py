#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    search and replace an element in a list
    Args:
        my_list - The list to search
        search - element to replace
        replace - subtitute for search
    """
    if my_list is None:
        return None
    return [replace if x == search else x for x in my_list]
