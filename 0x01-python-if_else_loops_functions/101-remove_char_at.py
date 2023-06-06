#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    count = 0
    for i in str:
        if (count == n):
            pass
        else:
            new_str = new_str + i
        count += 1
    return new_str
