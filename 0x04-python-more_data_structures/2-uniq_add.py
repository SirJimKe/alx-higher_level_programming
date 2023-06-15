#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    my_set = set(my_list)
    return sum(my_set)
