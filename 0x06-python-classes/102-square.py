#!/usr/bin/python3
""""Module to define Square class"""


class Square:
    """"Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init method"""
        self.size = size

    @property
    def size(self):
        """getter method for __size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter method for __size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method"""
        return self.size ** 2

    def __eq__(self, other):
        """equal comparison."""
        return self.__size == other.__size

    def __ne__(self, other):
        """equal comparison."""
        return self.__size != other.__size

    def __lt__(self, other):
        """equal comparison."""
        return self.__size < other.__size

    def __le__(self, other):
        """equal comparison."""
        return self.__size <= other.__size

    def __gt__(self, other):
        """equal comparison."""
        return self.__size > other.__size

    def __ge__(self, other):
        """equal comparison."""
        return self.__size >= other.__size
