class Square:
    def __init__(self, size=0): #initializing the class
        # raising exception
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
       #defining areag
    def area(self):
        return self.__size ** 2

    def perimeter(self):
        return 4 * self.__size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
