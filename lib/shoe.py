#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Initial condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            print("size must be an integer")
            return
        self._size = value

    def cobble(self):
        self.condition = "New"  # Set condition to "New" after cobbling
        print("Your shoe is as good as new!")
