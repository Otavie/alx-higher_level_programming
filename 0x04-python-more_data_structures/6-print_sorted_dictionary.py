#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    sorted_keys = sorted(a_dictionary)
    for a_key in sorted_keys:
        print(f"{a_key}: {a_dictionary[a_key]}")
