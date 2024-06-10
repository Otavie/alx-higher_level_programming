#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for each_key in a_dictionary:
            if each_key == key:
                a_dictionary[each_key] = value
    return a_dictionary
