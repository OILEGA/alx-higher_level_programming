#!/usr/bin/python3
"""Defining the class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """raises an exception when not implemented."""
        raise Exception("area() is not implemented")

