#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = [i for i in my_list]
    if (idx < 0 or idx >= len(my_list)):
        return (list_cp)
    else:
        list_cp[idx] = element
        return (list_cp)
