#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return ("{}".format(new_list))
    my_list[idx] = element
    return ("{}".format(my_list))
