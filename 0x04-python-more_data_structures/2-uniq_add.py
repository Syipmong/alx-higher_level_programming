#!/usr/bin/python3
"""dds all unique integers in a list only once for each integer"""


def uniq_add(my_list=[]):
    my_set = set(my_list)
    result = sum(my_set)
    return result
