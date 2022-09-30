#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    a function that returns the weighted average of all integers tuple
    """
    if my_list is None or my_list == []:
        return 0
    i_xy = sum(map(lambda a: a[0] * a[1], my_list))
    i_x = sum(map(lambda a: a[1], my_list))
    return i_xy / i_x
