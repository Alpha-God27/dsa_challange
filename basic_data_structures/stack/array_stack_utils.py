"""
===============================================================================
File Name   : array_stack_utils.py
Description : This module contains implementations of basic stack operations 
              using Python's list as the underlying storage (array-backed stack).
              It is part of fundamental data structure learning and covers:

              - Stack Creation
              - Push (insertion at top)
              - Pop (removal from top)
              - Peek (view top element)
              - Traversal (from bottom to top)
              - Size and Empty check
              - Reversing the stack
              - Rotating the stack elements

Author      : Prem Reddy
===============================================================================
"""

class StackArray:

    def __init__(self):
        self.arr = []

    def create_stack(self, initial_values=[]):
        """Initialize the stack with a list of values."""
        self.arr = list(initial_values) if initial_values else []

    def push(self, value):
        """Push an element to the top of the stack."""
        self.arr.append(value)

    def pop_value(self):
        """Pop the top element from the stack."""
        if self.arr:
            return self.arr.pop()
        else:
            print("Stack underflow: Cannot pop from an empty stack")
            return None

    def peek(self):
        """Peek at the top element of the stack."""
        if self.arr:
            print("Top most element is:", self.arr[-1])
            return self.arr[-1]
        else:
            print("Stack is empty")
            return None

    def traverse(self):
        """Print all elements from bottom to top."""
        if not self.arr:
            print("Stack is empty")
        else:
            print("Elements from bottom to top are:")
            for elem in self.arr:
                print(elem, end=" -> ")
            print("TOP")

    def size_empty_check(self):
        """Print size and whether stack is empty."""
        size = len(self.arr)
        if size == 0:
            print("Stack is empty")
            return False
        else:
            print("Size of stack is:", size)
            return True

    def reversing(self):
        """Reverse the stack in-place."""
        start, end = 0, len(self.arr) - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1

    def rotate(self, k=1):
        """
        Rotate the stack to the right by `k` steps.
        Brings the bottom `k` elements to the top in order.
        Example: [1, 2, 3, 4, 5], k=2 → [4, 5, 1, 2, 3]
        """
        n = len(self.arr)
        if n == 0 or k <= 0:
            return
        k = k % n
        self.arr = self.arr[-k:] + self.arr[:-k]


if __name__ == "__main__":
    s = StackArray()
    s.create_stack([1, 2, 3, 4, 5])
    print("Initial stack:")
    s.traverse()

    print("\nAfter push(6):")
    s.push(6)
    s.traverse()

    print("\nAfter pop_value():")
    popped = s.pop_value()
    print(f"Popped value: {popped}")
    s.traverse()

    print("\nPeeking top element:")
    s.peek()

    print("\nCheck size and emptiness:")
    s.size_empty_check()

    print("\nAfter reversing the stack:")
    s.reversing()
    s.traverse()

    print("\nAfter rotating stack by 2:")
    s.rotate(2)
    s.traverse()

    print("\nAfter rotating stack by 1:")
    s.rotate(1)
    s.traverse()
