#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is -ve r out of range
    if idx < 0 or idx >= len(my_list):
        return ("{}".format(my_list[:]))

    # Create a New List
    new_list = my_list[:]
    my_list[idx] = element
    return ("{}".format(my_list))
