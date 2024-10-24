'''
example for classes
'''

'''
-> "__init__" initilalize a cookie jar with the given "capacity" representing 
the max number of cookies that can fit in jar. If "capacity is negative int, "__init__"
should raise "ValueError"

-> "__str__" return a "str" with n "🍪", n is the number of cookies in the jar

-> "deposit" add "n" cookies to the jar. If adding that many would exceed the jar's capacity
"deposit" should raise a "ValueError"

-> "withdraw" remove "n" cookies from the jar. If there aren't that many cookies in the jar
"withdraw" should raise "ValueError"

-> "capacity" return the jar's capacity

-> "size" return the number of cookies actually in the jar, initially "0"
'''


class Jar:
    def __init__(self, capacity=12):

        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Deposit would exceed jar capacity")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer")
        if n > self._size:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    ...
