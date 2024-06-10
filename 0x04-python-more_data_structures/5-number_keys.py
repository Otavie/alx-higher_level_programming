#!/usr/bin/python3

def number_keys(a_dictionary):
    keys = []:
        for i in a_dictionary:
            keys.append(i[0])
    return len(keys)
