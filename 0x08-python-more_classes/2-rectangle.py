#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """using getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """using setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """using getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """using setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returning the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returning the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
