#!/usr/bin/python3
"""
This part would contain the lookup function
"""


def lookup(obj):
    """returns a list of all the attributes and methods of the 
       object including built-in attributes and methods."""
    return dir(obj)

