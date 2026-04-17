#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        my_list.count(i) > 1:
            new_list.append(i)
    return new_list
