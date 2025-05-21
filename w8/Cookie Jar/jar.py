class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an integer")
        if capacity < 0:
            raise ValueError("Capacity must be greater than or equal to 0")
        self._capacity = capacity
        self._size = 0
        

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            raise ValueError
        if self._size + n > self._capacity:
            raise ValueError
        
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            raise ValueError
        if self._size - n < 0:
            raise ValueError
        
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size