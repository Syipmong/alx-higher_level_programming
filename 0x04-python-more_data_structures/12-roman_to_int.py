#!/usr/bin/python3
def sub(num_list):
    to_sub = 0
    max_list = max(num_list)

    for i in num_list:
        if max_list > i:
            to_sub += i

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for c in roman_string:
        for r in list_keys:
            if r == c:
                if roman.get(c) <= last_roman:
                    number += sub(list_number)
                    list_number = [roman.get(c)]
                else:
                    list_number.append(roman.get(c))

                last_roman = roman.get(c)

    number += sub(list_number)

    return (number)
