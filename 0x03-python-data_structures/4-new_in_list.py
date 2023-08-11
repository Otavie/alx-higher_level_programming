#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return ("{}".format(my_list))
    if idx > len(my_list) - 1:
        return ("{}".format(new_list))
    else:
        my_list[idx] = element
        return ("{}".format(my_list))
