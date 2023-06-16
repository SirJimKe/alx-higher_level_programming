#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = dict(filter(lambda item: item[1] != value, a_dictionary.items()))
    return new_dict
