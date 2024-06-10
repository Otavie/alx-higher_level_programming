#!/usr/bin/python3

def number_keys(a_dictionary):
    the_keys = []
    for i in a_dictionary:
        the_keys.append(i[0])
    return len(the_keys)
