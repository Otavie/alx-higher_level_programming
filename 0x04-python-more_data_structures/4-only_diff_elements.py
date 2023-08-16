#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    all_elements = []
    for i in set_1:
        if i not in set_2:
            all_elements.append(i)
    for j in set_2:
        if j not in set_1:
            all_elements.append(j)
    return all_elements
