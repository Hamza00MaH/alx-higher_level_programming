#!/usr/bin/python3

def element_at(my_list, idx):
    if (idx < 0 or idx >= len(my_list)):
        return (None)
    index = 0
    for i in range(len(my_list)):
        if (index == idx):
            return (my_list[i])
        index = index + 1
