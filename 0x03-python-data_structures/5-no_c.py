#!/usr/bin/python3
def no_c(my_string):
    Nstr = ""
    for i in range(len(my_string)):
        if my_string[i] in "Cc":
            pass
        else:
            Nstr = Nstr + my_string[i]
    return (Nstr)
