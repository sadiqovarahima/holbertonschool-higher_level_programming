#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_integer = my_list[0]
        for digit in my_list:
            if digit > max_integer:
                max_integer = digit
        return max_integer
