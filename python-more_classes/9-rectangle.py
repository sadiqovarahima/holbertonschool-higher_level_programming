#!/usr/bin/python3
"""semedlesme"""


class Rectangle:
    """duzbucaqli klassi"""
    number_of_instance = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instance += 1
    
    @property
    def width(self):
        """eni geri qaytaririq"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """value yoxlanmasi"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        """eni geri qaytaririq"""
        return self.__height

    @height.setter
    def height(self, value):
        """value yoxlanmasi"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    def area(self):
        """sahe qaytarilmasi"""
        return self.__width * self.__height

    def perimeter(self):
        """perimetr qaytarilmasi"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol_
        return "\n".join([symbol * self.__width for i in range(self.__height)])
    def __repr__(self):
        """obyektin kod temsili"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """obyekt siliende mesaj versin"""
        Rectangle.number_of_imstance -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """boyuk olani qaytarir"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def square(cls, size=0):
        """eni hunndurluyu size olan rectangle qaytarir"""
        return cls(size, size)
