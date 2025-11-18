Stacks and Queues in Python - Complete Guide
Table of Contents

Stacks

What is a Stack?
Stack Operations
Stack Implementation
Stack Use Cases


Queues

What is a Queue?
Queue Operations
Queue Implementation
Queue Use Cases


Comparison
Real-World Examples


Stacks
What is a Stack?
A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle. Think of it like a stack of plates - you can only add or remove plates from the top.
Visual Representation
    Push →  ┌───┐
            │ 4 │  ← Top (last in, first out)
            ├───┤
            │ 3 │
            ├───┤
            │ 2 │
            ├───┤
            │ 1 │  ← Bottom
            └───┘
    Pop  ←
Key Characteristics

LIFO: Last In, First Out
Top: Only the top element is accessible
Two main operations: Push (add) and Pop (remove)

Stack Operations
OperationDescriptionTime Complexitypush(item)Add item to topO(1)pop()Remove and return top itemO(1)peek()View top item without removingO(1)is_empty()Check if stack is emptyO(1)size()Get number of elementsO(1)
Stack Implementation
Method 1: Using Python List
pythonclass Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def display(self):
        """Display all items in the stack"""
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):", self.items[::-1])


# Example Usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    stack.display()  # [4, 3, 2, 1]
    
    print(f"Top element: {stack.peek()}")  # 4
    print(f"Stack size: {stack.size()}")   # 4
    
    # Pop elements
    print(f"Popped: {stack.pop()}")  # 4
    print(f"Popped: {stack.pop()}")  # 3
    
    stack.display()  # [2, 1]
Method 2: Using collections.deque (More Efficient)
pythonfrom collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
Stack Use Cases
1. Parentheses Matching
pythondef is_balanced(expression):
    """Check if parentheses are balanced"""
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()

# Test
print(is_balanced("({[]})"))    # True
print(is_balanced("({[})"))     # False
print(is_balanced("((()))"))    # True
2. Reverse a String
pythondef reverse_string(text):
    """Reverse a string using a stack"""
    stack = Stack()
    
    # Push all characters
    for char in text:
        stack.push(char)
    
    # Pop all characters
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text

# Test
print(reverse_string("Hello"))  # "olleH"
3. Undo Functionality
pythonclass TextEditor:
    def __init__(self):
        self.text = ""
        self.history = Stack()
    
    def write(self, text):
        """Add text and save to history"""
        self.history.push(self.text)
        self.text += text
    
    def undo(self):
        """Undo last operation"""
        if not self.history.is_empty():
            self.text = self.history.pop()
    
    def display(self):
        print(f"Current text: {self.text}")

# Test
editor = TextEditor()
editor.write("Hello ")
editor.write("World")
editor.display()  # "Hello World"
editor.undo()
editor.display()  # "Hello "

Queues
What is a Queue?
A Queue is a linear data structure that follows the FIFO (First In, First Out) principle. Think of it like a line at a store - the first person in line is the first to be served.
Visual Representation
Enqueue →  ┌───┬───┬───┬───┐  → Dequeue
           │ 1 │ 2 │ 3 │ 4 │
           └───┴───┴───┴───┘
          Front         Rear
         (first out)  (last in)
Key Characteristics

FIFO: First In, First Out
Front: Where elements are removed
Rear: Where elements are added
Two main operations: Enqueue (add) and Dequeue (remove)

Queue Operations
OperationDescriptionTime Complexityenqueue(item)Add item to rearO(1)dequeue()Remove and return front itemO(1)front()View front item without removingO(1)is_empty()Check if queue is emptyO(1)size()Get number of elementsO(1)
Queue Implementation
Method 1: Using collections.deque (Recommended)
pythonfrom collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def display(self):
        """Display all items in the queue"""
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front to rear):", list(self.items))


# Example Usage
if __name__ == "__main__":
    queue = Queue()
    
    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    queue.display()  # [1, 2, 3, 4]
    
    print(f"Front element: {queue.front()}")  # 1
    print(f"Queue size: {queue.size()}")      # 4
    
    # Dequeue elements
    print(f"Dequeued: {queue.dequeue()}")  # 1
    print(f"Dequeued: {queue.dequeue()}")  # 2
    
    queue.display()  # [3, 4]
Method 2: Using Python List (Less Efficient)
pythonclass Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)  # O(n) - inefficient!
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
Method 3: Using queue.Queue (Thread-safe)
pythonfrom queue import Queue

# Built-in queue (thread-safe)
q = Queue()

q.put(1)      # Enqueue
q.put(2)
q.put(3)

print(q.get())  # 1 - Dequeue
print(q.get())  # 2
print(q.qsize())  # 1
Queue Use Cases
1. Task Scheduling
pythonclass TaskScheduler:
    def __init__(self):
        self.tasks = Queue()
    
    def add_task(self, task):
        """Add a task to the queue"""
        self.tasks.enqueue(task)
        print(f"Task added: {task}")
    
    def process_next(self):
        """Process the next task"""
        if not self.tasks.is_empty():
            task = self.tasks.dequeue()
            print(f"Processing: {task}")
        else:
            print("No tasks to process")
    
    def show_tasks(self):
        """Show all pending tasks"""
        self.tasks.display()

# Test
scheduler = TaskScheduler()
scheduler.add_task("Send email")
scheduler.add_task("Generate report")
scheduler.add_task("Update database")
scheduler.show_tasks()
scheduler.process_next()  # Processes "Send email" first
2. Breadth-First Search (BFS)
pythondef bfs(graph, start):
    """Breadth-First Search using a queue"""
    visited = set()
    queue = Queue()
    queue.enqueue(start)
    visited.add(start)
    result = []
    
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    
    return result

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
3. Print Queue
pythonclass PrintQueue:
    def __init__(self):
        self.queue = Queue()
    
    def add_document(self, document):
        """Add a document to print queue"""
        self.queue.enqueue(document)
        print(f"Added to queue: {document}")
    
    def print_next(self):
        """Print the next document"""
        if not self.queue.is_empty():
            doc = self.queue.dequeue()
            print(f"Printing: {doc}")
        else:
            print("No documents in queue")
    
    def show_queue(self):
        """Show all documents in queue"""
        self.queue.display()

# Test
printer = PrintQueue()
printer.add_document("Report.pdf")
printer.add_document("Invoice.pdf")
printer.add_document("Memo.pdf")
printer.show_queue()
printer.print_next()  # Prints "Report.pdf" first

Comparison
Stack vs Queue
FeatureStackQueuePrincipleLIFO (Last In, First Out)FIFO (First In, First Out)InsertionPush at topEnqueue at rearDeletionPop from topDequeue from frontAccessTop onlyFront onlyReal-world analogyStack of platesLine at a storeUse casesUndo/Redo, Function calls, Expression evaluationTask scheduling, BFS, Print queue
Visual Comparison
STACK (LIFO):
Push: 1 → 2 → 3 → 4
Pop:  4 → 3 → 2 → 1
      ↑
      Last in, first out

QUEUE (FIFO):
Enqueue: 1 → 2 → 3 → 4
Dequeue: 1 → 2 → 3 → 4
         ↑
         First in, first out

Real-World Examples
Stack Examples

Browser History - Back button (last visited page first)
Undo/Redo - Text editors, Photoshop
Function Call Stack - How programs execute functions
Expression Evaluation - Converting infix to postfix
Backtracking - Maze solving, chess moves

Queue Examples

Customer Service - First customer served first
Print Spooler - Documents printed in order
CPU Scheduling - Process management
Breadth-First Search - Graph traversal
Call Center - Calls answered in order received


Additional Data Structures
Priority Queue
Elements are dequeued based on priority, not insertion order.
pythonimport heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, item, priority):
        """Add item with priority (lower number = higher priority)"""
        heapq.heappush(self.heap, (priority, item))
    
    def dequeue(self):
        """Remove and return highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return heapq.heappop(self.heap)[1]
    
    def is_empty(self):
        return len(self.heap) == 0

# Test
pq = PriorityQueue()
pq.enqueue("Low priority task", 3)
pq.enqueue("High priority task", 1)
pq.enqueue("Medium priority task", 2)

print(pq.dequeue())  # "High priority task" (priority 1)
print(pq.dequeue())  # "Medium priority task" (priority 2)
Circular Queue
A queue where the last position connects back to the first.
pythonclass CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        
        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        
        item = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return item

Performance Summary
Time Complexity
OperationStackQueue (deque)Queue (list)Push/EnqueueO(1)O(1)O(1)Pop/DequeueO(1)O(1)O(n) ❌Peek/FrontO(1)O(1)O(1)SizeO(1)O(1)O(1)
Recommendation: Use collections.deque for queues in Python!

Complete Working Examples
Stack Example: Calculator
pythondef evaluate_postfix(expression):
    """Evaluate postfix expression using stack"""
    stack = Stack()
    
    for char in expression.split():
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
    
    return stack.pop()

# Test: "3 4 + 2 * 7 /" = ((3 + 4) * 2) / 7 = 2
print(evaluate_postfix("3 4 + 2 * 7 /"))  # 2.0
Queue Example: Hot Potato Game
pythondef hot_potato(names, num):
    """Simulate hot potato game"""
    queue = Queue()
    
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        
        eliminated = queue.dequeue()
        print(f"{eliminated} is out!")
    
    return queue.dequeue()

# Test
players = ["Alice", "Bob", "Charlie", "David", "Eve"]
winner = hot_potato(players, 7)
print(f"Winner: {winner}")

Resources

Python collections.deque Documentation https://docs.python.org/3/library/collections.html#collections.deque 
Python queue Module Documentation https://docs.python.org/3/library/queue.html 
Big O Cheat Sheet https://www.bigocheatsheet.com/ 
Visualize Stacks and Queues https://visualgo.net/en/list 


Created for learning data structures in Python 🐍