#!/usr/bin/python3
def magic_string(count=[0]):
    count[0] += 1
    return "BestSchool, " * (count[0] - 1) + "BestSchool"
