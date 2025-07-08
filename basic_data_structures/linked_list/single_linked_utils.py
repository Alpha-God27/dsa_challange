"""
===============================================================================
File Name   : singly_linked_list_utils.py
Description : This module contains implementations of basic singly linked list 
              operations using user-defined Node and LinkedList classes. It is 
              part of fundamental data structure learning and covers:

              - Node and List Initialization
              - Insertion at beginning, end, and specific position
              - Deletion by value and by position
              - Traversal and printing
              - Searching for a value
              - Reversing the list (iterative and recursive)
              - Finding length (iterative and recursive)
              - Rotating the list (by k nodes)
              - Getting nth node from start or end
              - Utility: convert to Python list, clear list

Author      : Prem Reddy
===============================================================================
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.node = None

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def inser_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def insert_at_middle(self, pos, value):
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.head
        current_pos = 0
        while node is not None and current_pos < pos - 1:
            node = node.next
            current_pos += 1
        if node is None:
            print("Position out of bounds.")
            return False
        new_node.next = node.next
        node.next = new_node
        return True

    def delete_by_value(self, value):
        node = self.head
        previous = None
        while node is not None:
            if node.value == value:
                if previous is None:
                    self.head = node.next
                else:
                    previous.next = node.next
                return True  
            previous = node
            node = node.next

        return False

    def delete_by_index(self, index):
        node = self.head
        previous = None
        pos = 0
        while node is not None:
            if pos == index:
                if previous is None:
                    self.head = node.next 
                else:
                    previous.next = node.next  
                return True 
            previous = node
            node = node.next
            pos += 1

        return False

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.value, "->", end=" ")
            node = node.next
        print("None")

    def search(self, value):
        node = self.head
        pos = 0
        while node is not None:
            if node.value == value:
                print("Value %s is at position %s",value,pos)
                return
            node = node.next
            pos += 1
        print("Value %s not found in the list",value)

    def iterative_reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next     
            current.next = previous      
            previous = current           
            current = next_node          
        self.head = previous  
    
    def recursive_reverse(self):
        def _reverse_recursive(current, previous):
            if current is None:
                return previous
            next_node = current.next
            current.next = previous
            return _reverse_recursive(next_node, current)

        self.head = _reverse_recursive(self.head, None)

    def len_find_iter(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1

        print(f"Length of the linked list is: {length}")

    def len_find_recur(self):
        def _recursive_len(current):
            if current is None:
                return 0
            return 1 + _recursive_len(current.next)

        count = _recursive_len(self.head)
        print(f"Length of the linked list is: {count}")


    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


    def clear(self):
        self.head = None

    def get_nth_node_from_start(self, n):
        current = self.head
        index = 0
        while current:
            if index == n:
                return current.value
            index += 1
            current = current.next
        return None  # Out of bounds


    def get_nth_node_from_end(self, n):
        fast = self.head
        slow = self.head
        for _ in range(n):
            if fast is None:
                return None  
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        return slow.value if slow else None

    def rotate(self, k):
        if self.head is None or k == 0:
            return
        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1
        k = k % length
        if k == 0:
            return  # No change

        current = self.head
        for _ in range(length - k - 1):
            current = current.next

        new_head = current.next
        current.next = None

        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = self.head
        self.head = new_head

if __name__ == "__main__":
    print("\n===== Singly Linked List Demo =====")
    sll = SingleLinkedList()

    print("\n→ Inserting at start:")
    sll.inser_at_start(30)
    sll.inser_at_start(20)
    sll.inser_at_start(10)
    sll.traverse()

    print("\n→ Inserting at end:")
    sll.insert_at_end(40)
    sll.insert_at_end(50)
    sll.traverse()

    print("\n→ Inserting at position 3:")
    sll.insert_at_middle(3, 35)
    sll.traverse()

    print("\n→ Delete by value 20:")
    sll.delete_by_value(20)
    sll.traverse()

    print("\n→ Delete by index 2:")
    sll.delete_by_index(2)
    sll.traverse()

    print("\n→ Search for value 35:")
    sll.search(35)

    print("\n→ Search for value 99:")
    sll.search(99)

    print("\n→ Iterative reverse:")
    sll.iterative_reverse()
    sll.traverse()

    print("\n→ Recursive reverse:")
    sll.recursive_reverse()
    sll.traverse()

    print("\n→ Length (iterative):")
    sll.len_find_iter()

    print("\n→ Length (recursive):")
    sll.len_find_recur()

    print("\n→ Get 2nd node from start:")
    print("Value:", sll.get_nth_node_from_start(2))

    print("\n→ Get 2nd node from end:")
    print("Value:", sll.get_nth_node_from_end(2))

    print("\n→ Rotate by 2:")
    sll.rotate(2)
    sll.traverse()

    print("\n→ Convert to list:")
    print(sll.to_list())

    print("\n→ Clear list:")
    sll.clear()
    sll.traverse()
