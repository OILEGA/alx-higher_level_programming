#!/usr/bin/python3
"""
Contains the inherited class function
"""


def inherits_from(obj, a_class):
    """returns true if object is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)

