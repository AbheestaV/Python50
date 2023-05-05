class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity >=0:
            self._capacity = capacity
        else:
            raise ValueError("Not enough cookies")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size <= self.capacity:
            self._size = size
        else:
            raise ValueError("Too many cookies")
        if self._size < 0:
            raise ValueError

