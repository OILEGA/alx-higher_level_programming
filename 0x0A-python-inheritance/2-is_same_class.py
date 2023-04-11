#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """If obj is the exact class a_class return true, otherwise false"""
    return (type(obj) == a_class)

