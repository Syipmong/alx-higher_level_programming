#!/usr/bin/python3
"""a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary)
    for key in sorted_key:
        print("{}: {}".format(key, a_dictionary[key]))
