class Jar:
    """Jar base class"""
    def __init__(self, capacity: int=12):
        self.size = 0
        self.capacity = capacity # use setter


    def deposit(self, v):
        if self.__size + v > self.__capacity:
            raise ValueError
        else:
            self.__size += v


    def withdraw(self, v):
        if v > self.__size:
            raise ValueError
        else:
            self.__size -= v

    def __str__(self):
        cockie = "🍪"
        return(cockie * self.__size)
    
    def __repr__(self):
        return self.__str__

    @property
    def capacity(self):
        return (self.__capacity)

    @capacity.setter
    def capacity(self, a):
        a = int(a)
        if a < 0:
            raise ValueError
        self.__capacity = a


    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, a):
        self.__size = a
