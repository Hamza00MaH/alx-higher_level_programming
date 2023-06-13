#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if (length > 0):
        f_char = sentence[0]
    else:
        f_char = None
    return (length, f_char)
