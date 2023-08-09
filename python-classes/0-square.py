#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
    #getting the area
    def area(self):
        return self.__size ** 2
    # getting the perimeter
    def perimeter(self):
        return 4 * self.__size
    # getting the size
    def get_size(self):
        return self.__size
     # setting the size
    def set_size(self, size):
        self.__size = size


