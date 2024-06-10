#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for a_key in a_dictionary:
        new_dictionary[a_key] = a_dictionary[a_key] * 2
    return new_dictionary
