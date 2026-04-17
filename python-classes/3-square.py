#!/usr/bin/python3
"""Define a square based on given info"""
class Square:
    """Define a square in the system."""
    def __init__(self, size=0):
        """Args: size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size**2
