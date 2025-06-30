"""
===============================================================================
File Name   : array_utils.py
Description : This module contains implementations of basic array operations 
              as part of fundamental data structure learning. It covers:
              
              - Creation
              - Insertion (beginning, middle, end)
              - Deletion (by index, by value)
              - Traversal
              - Searching (linear and binary)
              - Updating values
              - Utility functions for demonstration

Author      : Prem Reddy
===============================================================================
"""

class Array:
    def __init__(self):
        self.arr = []

    def creation(self, initial_values=None):
        self.arr = initial_values if initial_values else []

    def insert_beginning(self, value):
        self.arr.insert(0, value)

    def insert_middle(self, index, value):
        if 0 <= index <= len(self.arr):
            self.arr.insert(index, value)
        else:
            print("Index out of bounds.")

    def insert_ending(self, value):
        self.arr.append(value)

    def delete_by_index(self, index):
        if 0 <= index < len(self.arr):
            self.arr.pop(index)
        else:
            print("Index out of bounds.")

    def delete_by_value(self, value):
        if value in self.arr:
            self.arr.remove(value)
        else:
            print("Value not found in array.")

    def traverse(self):
        for item in self.arr:
            print(item, end=" ")
        print()

    def linear_search(self, value):
        for i, item in enumerate(self.arr):
            if item == value:
                return i
        return -1

    def binary_search(self, value):
        low, high = 0, len(self.arr) - 1
        self.arr.sort()  # Binary search requires sorted array
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def updating_value_by_index(self, index, new_value):
        if 0 <= index < len(self.arr):
            self.arr[index] = new_value
        else:
            print("Index out of bounds.")

    def updating_values_by_value(self, old_value, new_value):
        found = False
        for i in range(len(self.arr)):
            if self.arr[i] == old_value:
                self.arr[i] = new_value
                found = True
        if not found:
            print("Value not found in array.")


if __name__ == "__main__":
    a = Array()
    a.creation([1, 2, 3, 4, 5])
    print("Initial array:")
    a.traverse()

    a.insert_beginning(0)
    print("After insert_beginning(0):")
    a.traverse()

    a.insert_middle(3, 99)
    print("After insert_middle(3, 99):")
    a.traverse()

    a.insert_ending(100)
    print("After insert_ending(100):")
    a.traverse()

    a.delete_by_index(2)
    print("After delete_by_index(2):")
    a.traverse()

    a.delete_by_value(99)
    print("After delete_by_value(99):")
    a.traverse()

    index = a.linear_search(4)
    print(f"Linear search for 4 found at index: {index}")

    index = a.binary_search(100)
    print(f"Binary search for 100 found at index: {index}")

    a.updating_value_by_index(0, 111)
    print("After updating index 0 to 111:")
    a.traverse()

    a.updating_values_by_value(5, 555)
    print("After updating value 5 to 555:")
    a.traverse()