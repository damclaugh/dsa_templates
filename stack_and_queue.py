
# QUEUE
# FIFO structure
# enqueue/append to the end to add element
# dequeue/pop at the front to remove element

# enqueue and dequeue take O(1) time

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)



# TEST CASES
q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)

print(q.size()) # prints 3
q.display() # prints [1, 3, 5]
q.dequeue()
print(q.size()) # prints 2
q.display() # prints [3, 5]



# STACK
# LIFO data structure
# push/append to the top to add element
# pop from the top to remove element
# pop and push take O(1) time

class Stack:
    def __init__(self):
        self.items = []
    
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
        print(self.items)


# TEST CASES
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display() # prints [1, 2, 3]
print(s.size()) # prints 3
s.pop()
s.display() # prints [1, 2]