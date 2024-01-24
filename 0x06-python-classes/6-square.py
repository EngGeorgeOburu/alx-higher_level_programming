#!/usr/bin/python3
class Square:
    """ Square  Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Init method initilaizes the the size of the square
        Attributes:
            size: Size of the square
            position: Position of the square
        Raises:
            TypeError: If size ! int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if self.__check_tuple(position) is False \
                or self.__check_indexes(position) is False \
                or self.__check_integers(position) is False \
                or self.__check_values(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position
    """
    Get method retrieves the size of the square
    Returns:
    int: size of the square
    """
    @property
    def size(self):
        return self.__size
    """
    Setter method sets the size of the square
    Raises:
    TypeError: If size is not an integer
    ValueError: If size is less than 0
    """
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    Getter method for retrieving the position of the square
    """
    @property
    def position(self):
        return self._position
    """ Setter method for setting the position of the square
    Raises:
    TypeError:If position is not a tuple
    """
    @position.setter
    def position(self, position):
        if position.__check_tuple(position) is False \
                or position.__check_indexes(position) is False \
                or position.__check_integers(position) is False \
                or position.__check_values(position) is False:
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = position
    """ Checks if tupleis in position
    """
    def __check_tuple(self, position):
        if type(position) is tuple:
            return True

        return False
    """
    Checks if the index are in position
    """
    def __check__indexes(self, position):
        if len(position) == 2:
            return True
        return False
    """
    Checks if interes
    """
    def __check_integers(self, position):
        if position[0] is int and type(position[1]) is int:
            return True
        return False
    """ Check if the values are in position
    """
    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False
    """
    Calculate the area of the square
    """
    def area(self):
        return self.__size ** 2
    """
    Prints the positions using special character '#'
    """
    def my_print(self):
        if self.__size == 0:
            print()
            return None
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')
        if j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}'.format('#', w=self.__position[0] + 1), end="")
            else:
                print('#', end='')
            if j % self.__size == 0 and j > 0:
                print()
