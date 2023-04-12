#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """would return the number of characters written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
