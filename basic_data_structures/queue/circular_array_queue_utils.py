"""
===============================================================================
File Name   : circular_array_queue_utils.py
Description : This module contains implementations of basic circular queue 
              operations using a fixed-size Python list as the underlying 
              storage (array-backed circular queue). It is part of fundamental 
              data structure learning and covers:

              - Circular Queue Initialization (with fixed capacity)
              - Enqueue (insertion at rear with wrap-around)
              - Dequeue (removal from front with wrap-around)
              - Peek (view front element)
              - Traversal (from front to rear respecting circular order)
              - Size and Empty/Full checks
              - Reversing the circular queue
              - Rotating the queue elements within capacity bounds

Author      : Prem Reddy
===============================================================================
"""

class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed = self.queue[self.front]
        self.queue[self.front] = None  # Optional cleanup
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = -1
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    def traversal(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        index = self.front
        for _ in range(self.size):
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
        print()

    def get_size(self):
        print(f"Queue size: {self.size}")
        return self.size

    def reversing(self):
        if self.is_empty():
            print("Queue is empty. Nothing to reverse.")
            return
        elements = []
        index = self.front
        for _ in range(self.size):
            elements.append(self.queue[index])
            index = (index + 1) % self.capacity
        elements.reverse()
        index = self.front
        for val in elements:
            self.queue[index] = val
            index = (index + 1) % self.capacity
        print("Queue reversed.")

    def rotate(self, k):
        if self.is_empty():
            print("Queue is empty. Cannot rotate.")
            return
        k = k % self.size
        if k == 0:
            print("Rotation not needed.")
            return
        elements = []
        index = self.front
        for _ in range(self.size):
            elements.append(self.queue[index])
            index = (index + 1) % self.capacity
        elements = elements[k:] + elements[:k]
        index = self.front
        for val in elements:
            self.queue[index] = val
            index = (index + 1) % self.capacity
        print(f"Queue rotated by {k} positions.")


# ======================== DEMO ===========================
if __name__ == "__main__":
    cq = CircularQueue(5)

    print("\n--- Enqueue Operations ---")
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)
    cq.enqueue(60)  # Should fail

    print("\n--- Traversal ---")
    cq.traversal()

    print("\n--- Peek ---")
    cq.peek()

    print("\n--- Dequeue Operations ---")
    cq.dequeue()
    cq.dequeue()

    print("\n--- Traversal After Dequeue ---")
    cq.traversal()

    print("\n--- Enqueue After Wrap-Around ---")
    cq.enqueue(60)
    cq.enqueue(70)

    print("\n--- Final Queue State ---")
    cq.traversal()

    print("\n--- Reverse the Queue ---")
    cq.reversing()
    cq.traversal()

    print("\n--- Rotate the Queue by 2 ---")
    cq.rotate(2)
    cq.traversal()

    print("\n--- Size Check ---")
    cq.get_size()

    print("\n--- Dequeue Remaining Elements ---")
    while not cq.is_empty():
        cq.dequeue()

    print("\n--- Final State After Emptied ---")
    cq.traversal()
