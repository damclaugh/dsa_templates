
# QUEUE
# FIFO structure
# enqueue/append to the end to add element
# dequeue/pop at the front to remove element

# enqueue is O(1) time complexity
# dequeue is O(n) time complexity

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def display(self):
        return self.items



# TEST CASES
q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)

print(q.size()) # 3
q.display() # [1, 3, 5]
q.dequeue()
print(q.is_empty()) # False
print(q.size()) # 2
q.display() # [3, 5]



# STACK
# LIFO data structure
# push/append to the top to add element
# pop from the top to remove element
# pop and push take O(1) time

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.size() == 0
    
    def push(self, item):
        self.items.append(item)
    
    # remove and return last item
    def pop(self):
        if self.size() == 0:
            return None
        else:
            self.items.pop()

    # get last item w/o removing it
    def peek(self):
        if self.size() == 0:
            return None

        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


# TEST CASES
s = Stack()
s.push(1)
print(s.is_empty()) # False
s.push(2)
s.push(3)
s.display() # [1, 2, 3]
print(s.size()) # 3
s.pop()
s.display() # [1, 2]