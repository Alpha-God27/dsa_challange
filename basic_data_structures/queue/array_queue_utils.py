"""
===============================================================================
File Name   : array_queue_utils.py
Description : This module contains implementations of basic queue operations 
              using Python's list as the underlying storage (array-backed queue).
              It is part of fundamental data structure learning and covers:

              - Queue Creation
              - Enqueue (insertion at rear)
              - Dequeue (removal from front)
              - Peek (view front element)
              - Traversal (from front to rear)
              - Size and Empty check
              - Reversing the queue
              - Rotating the queue elements

Author      : Prem Reddy
===============================================================================
"""

class Queue:
    
    def __init__(self):
        self.arr = []

    def create_queue(self, initial_values=None):
        self.arr = initial_values if initial_values else []

    def enqueue(self, value):
        self.arr.append(value)

    def dequeue(self):
        if not self.arr:
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.arr.pop(0)

    def peek(self):
        if not self.arr:
            print("Queue is empty.")
            return None
        print(self.arr[0])

    def traversal(self):
        print(self.arr)

    def size_empty_check(self):
        if not self.arr:
            print("Queue is empty.")
        else:
            print(f"Size of queue: {len(self.arr)}")

    def reversing(self):
        start, end = 0, len(self.arr) - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1

    def rotate(self, k=1):
        if not self.arr:
            print("Queue is empty.")
            return
        k = k % len(self.arr)  # handle over-rotation
        self.arr = self.arr[k:] + self.arr[:k]
