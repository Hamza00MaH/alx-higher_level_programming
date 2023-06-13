#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis_t = []
    for i in my_list:
        if (i % 2 == 0):
            lis_t.append(True)
        else:
            lis_t.append(False)
    return (lis_t)
