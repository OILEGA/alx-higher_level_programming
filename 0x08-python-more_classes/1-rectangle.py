

#!/usr/bin/python3

class Rectangle:
    def __init__(self, width = 0, height = 0):

        self.width = width
        self.height = height

"""  using the getter for private instance attribute width """

    
@property


def width(self):
    return self.__width
""" using the setter for private instance attribute width """
@width.setter

def width(self, value):
    if type(value) is not int:
        raise TypeError("width must be an integer")
    elif value < 0:
        raise ValueError("width must be >= 0")
        self.__width = value

""" using the getter for private instance attribute height """
@property
def height(self):
    return self.__height

""" using the setter private instance attribute height """
@height.setter

def height(self, value):
    if type(value) is not int:
        raise TypeError("height must be an integer")
    elif value < 0:
        raise ValueError(" height must be >= 0")
        self.__height = value	 