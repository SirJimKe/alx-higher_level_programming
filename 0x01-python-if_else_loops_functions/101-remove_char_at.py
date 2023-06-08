#!/usr/bin/python3

def remove_char_at(str, n):
    """removes a character at the position n"""
    string = ""
    for i, char in enumerate(str):
        if i == n:
            continue
        else:
            string += char
    return string
