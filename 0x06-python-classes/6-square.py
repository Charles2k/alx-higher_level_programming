#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Privatize instance attribute: size with optional"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Initialize size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set conditions for size attribute and raise exceptions"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Initialize position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set conditions for position attribute and raise exceptions"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Find the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print a square filled with #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
