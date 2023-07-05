#!/usr/bin/python3
""" Defines LockedClass Class """


class LockedClass:
    """
    prevents the dynamic creation of new instance attributes,
    except for first_name
    """
    __slots__ = ["first_name"]
