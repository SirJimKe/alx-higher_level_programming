#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string"""
    my_list = []
    for char in my_string:
        if char != 'c' and char != 'C':
            my_list.append(char)
    new_string = ''.join(my_list)
    return new_string
