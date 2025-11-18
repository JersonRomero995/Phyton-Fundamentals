Linked Lists in Python - Complete Guide
Table of Contents

What is a Linked List?
Visual Representation
Implementation
Basic Operations
Complete Example
Comparison with Python Lists
When to Use Linked Lists
Types of Linked Lists

What is a Linked List?
A linked list is a linear data structure where elements (called nodes) are connected like a chain. Each node contains:

Data - the value you want to store
Next - a reference/pointer to the next node

Unlike arrays where elements are stored in contiguous memory locations, linked list nodes can be stored anywhere in memory, connected through pointers.
Visual Representation
Regular Python List (Array):
┌────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │  ← Contiguous memory
└────┴────┴────┴────┘

Linked List:
┌────┬────┐    ┌────┬────┐    ┌────┬────┐    ┌────┬──────┐
│ 10 │ ●──┼───→│ 20 │ ●──┼───→│ 30 │ ●──┼───→│ 40 │ None │
└────┴────┘    └────┴────┘    └────┴────┘    └────┴──────┘
 data  next      data  next      data  next      data  next
Implementation
Node Class
The building block of a linked list:
pythonclass Node:
    def __init__(self, data):
        self.data = data  # Stores the value
        self.next = None  # Points to the next node (initially None)
LinkedList Class
The main class that manages the linked list:
pythonclass LinkedList:
    def __init__(self):
        self.head = None  # The first node (initially empty)
Basic Operations
1. Insert at Beginning - O(1)
pythondef insert_at_beginning(self, data):
    """Insert a new node at the beginning of the list"""
    new_node = Node(data)      # Create new node
    new_node.next = self.head  # Point new node to current head
    self.head = new_node       # Make new node the new head
Example:
pythonll = LinkedList()
ll.insert_at_beginning(30)  # [30|None]
ll.insert_at_beginning(20)  # [20]→[30|None]
ll.insert_at_beginning(10)  # [10]→[20]→[30|None]
2. Insert at End - O(n)
pythondef insert_at_end(self, data):
    """Insert a new node at the end of the list"""
    new_node = Node(data)
    
    # If list is empty, make new node the head
    if self.head is None:
        self.head = new_node
        return
    
    # Traverse to the last node
    current = self.head
    while current.next:
        current = current.next
    
    # Link the last node to new node
    current.next = new_node
3. Insert at Position - O(n)
pythondef insert_at_position(self, data, position):
    """Insert a new node at a specific position"""
    new_node = Node(data)
    
    # If inserting at beginning
    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return
    
    # Traverse to the position
    current = self.head
    for i in range(position - 1):
        if current is None:
            print("Position out of bounds")
            return
        current = current.next
    
    # Insert the node
    new_node.next = current.next
    current.next = new_node
4. Delete a Node - O(n)
pythondef delete(self, key):
    """Delete the first node with the given key"""
    current = self.head
    
    # If head node contains the key
    if current and current.data == key:
        self.head = current.next
        current = None
        return
    
    # Search for the node to delete
    prev = None
    while current and current.data != key:
        prev = current
        current = current.next
    
    # If key was not found
    if current is None:
        print(f"Key {key} not found in the list")
        return
    
    # Unlink the node from the list
    prev.next = current.next
    current = None
5. Search - O(n)
pythondef search(self, key):
    """Search for a node with the given key"""
    current = self.head
    position = 0
    
    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1
    
    return -1  # Not found
6. Display the List - O(n)
pythondef display(self):
    """Display all nodes in the list"""
    if self.head is None:
        print("List is empty")
        return
    
    current = self.head
    while current:
        print(current.data, end=" → ")
        current = current.next
    print("None")
7. Get Length - O(n)
pythondef get_length(self):
    """Return the number of nodes in the list"""
    count = 0
    current = self.head
    
    while current:
        count += 1
        current = current.next
    
    return count
Complete Example
pythonclass Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete(self, key):
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next
        current = None
    
    def search(self, key):
        current = self.head
        position = 0
        
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
    
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Example Usage
if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()
    
    # Insert elements
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    
    print("Linked List:")
    ll.display()  # Output: 5 → 10 → 20 → 30 → None
    
    print(f"\nLength: {ll.get_length()}")  # Output: 4
    
    # Search for an element
    position = ll.search(20)
    if position != -1:
        print(f"Element 20 found at position {position}")
    
    # Delete an element
    ll.delete(20)
    print("\nAfter deleting 20:")
    ll.display()  # Output: 5 → 10 → 30 → None
Comparison with Python Lists
OperationLinked ListPython List (Array)Insert at beginningO(1) ✅O(n)Insert at endO(n)O(1) ✅Insert at positionO(n)O(n)Delete elementO(n)O(n)Access by indexO(n)O(1) ✅SearchO(n)O(n)Memory usageMore (stores data + pointer)Less (only data)
When to Use Linked Lists
✅ Good for:

Frequent insertions/deletions at the beginning
Dynamic size (don't know size in advance)
Implementing stacks and queues
Don't need random access by index
Memory fragmentation is acceptable

❌ Not good for:

Need frequent access by index
Memory is limited (extra overhead for pointers)
Need cache-friendly data structures
Simple sequential access (Python lists are faster)

Types of Linked Lists
1. Singly Linked List
Each node points only to the next node (what we covered above).
[A]→[B]→[C]→[D]→None
2. Doubly Linked List
Each node points to both next and previous nodes.
None←[A]⇄[B]⇄[C]⇄[D]→None
3. Circular Linked List
The last node points back to the first node.
[A]→[B]→[C]→[D]→(back to A)
Additional Resources

Python Data Structures Documentation https://docs.python.org/3/tutorial/datastructures.html 
Big O Notation Cheat Sheet https://www.bigocheatsheet.com/ 
Visualize Data Structures https://visualgo.net/en/list 

License
This guide is open source and available for educational purposes.