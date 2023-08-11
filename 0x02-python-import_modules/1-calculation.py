#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, div, mul
    """give the result from the different calculation processes"""
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
