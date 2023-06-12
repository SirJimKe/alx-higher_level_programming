#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in list"""
    if 0 <= idx < len(my_list):
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    else:
        return my_list[:]
