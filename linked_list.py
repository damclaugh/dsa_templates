

# lookup, insert and delete are O(n) time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    # outputs to list
    def to_list(self):
        out_list = []
        cur_node = self.head
        while cur_node:
            out_list.append(cur_node.value)
            cur_node = cur_node.next
        
        return out_list

    # adds to tail
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    # add to beginning of list
    def prepend(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node
    
    # add after specific node
    def insert_after_node(self, prev_node, value):
        
        if not prev_node:
            print('Previous node not in list')
            return

        new_node = Node(value)
        new_node.next = prev_node.next # new node points to the next node (ie previous node's next)
        prev_node.next = new_node

    # insert at index
    def insert_pos(self, value, pos):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        cur_node = self.head
        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None: # reached end of list
            return

        new_node.next = prev_node.next # new node points to the next node (ie previous node's next)
        prev_node.next = new_node

    def search(self, value):
        cur_node = self.head
        
        while cur_node:
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False

    def delete_node(self, value):
        # deletes value if it's at the head
        while self.head is not None and self.head.value == value:
            self.head = self.head.next
        
        cur_node = self.head
        while cur_node and cur_node.next:
            if cur_node.next.value == value:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
            
        return self.head

    # alternative delete method
    def delete_node2(self, value):
        cur_node = self.head
        prev_node = None

        while cur_node:
            # if value found, skip over it and keep going
            if cur_node.value == value:
                if prev_node: # in the middle of the list somewhere
                    prev_node.next = cur_node.next
                    cur_node.next = None
                    cur_node = prev_node.next
                    
                else: # still at the head
                    self.head = cur_node.next
                    cur_node = self.head
            else:
                prev_node = cur_node
                cur_node = cur_node.next

        if cur_node is None: # value isn't in list
            return

    # delete at index
    def delete_pos(self, pos):
        cur_node = self.head

        # if head is being deleted
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None: # reached end of list
            return

        prev_node.next = cur_node.next
        cur_node = None

    def get_ith(self, i): # get element at index i
        cur_node = self.head
        
        count = 0
        while cur_node:
            if count == i:
                return cur_node.value
            count += 1
            cur_node = cur_node.next

        if cur_node is None:
            print('Position not in list')
            return

    # A -> B -> C 
    # if on B, B.next should point to A
    def reverse_list(self):
        cur_node = self.head
        prev_node = None
       
        while cur_node:
            nxt = cur_node.next # temporary pointer to point to next node
            cur_node.next = prev_node # flips arrow
            prev_node = cur_node # makes current node the previous node
            cur_node = nxt
        self.head = prev_node # reset head so it points to C (A <- B <- C)

    def detect_loop(self):
        s = set()
        cur_node = self.head
        
        while cur_node:
            if cur_node in s:
                return True
            s.add(cur_node)
            cur_node = cur_node.next
        
        return False

    



llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
print(llist.to_list()) # ['A', 'B', 'C', 'D']
llist.insert_after_node(llist.head.next, 'E') # insert after B
print(llist.to_list()) # ['A', 'B', 'E', 'C', 'D']
llist.delete_node('B') 
print(llist.to_list()) # ['A', 'E', 'C', 'D']
print(llist.search('C')) # True
print(llist.search('B')) # False
print(llist.get_ith(3)) # 'D'
llist.delete_pos(2)
print(llist.to_list()) # ['A', 'E', 'D']
llist.insert_pos('C', 2)
print(llist.to_list()) # ['A', 'E', 'C', 'D']
print(llist.get_ith(2)) # 'C'
llist.reverse_list()
print(llist.to_list()) # ['D', 'C', 'E', 'A']
llist.prepend('Z')
print(llist.to_list()) # ['Z', 'D', 'C', 'E', 'A']
llist.append('D')
print(llist.to_list()) # ['Z', 'D', 'C', 'E', 'A', 'D']
llist.delete_node('D')
print(llist.to_list()) # ['Z', 'C', 'E', 'A']
llist.delete_node('Z')
print(llist.to_list()) # ['C', 'E', 'A']
llist.append('A')
print(llist.to_list()) # ['C', 'E', 'A', 'A']
llist.delete_node2('A')
print(llist.to_list()) # ['C', 'E']

llist2 = LinkedList()
llist2.append(20)
llist2.append(4)
llist2.append(15)
llist2.append(10)
llist2.head.next.next.next.next = llist2.head
print(llist2.detect_loop()) # True

llist3 = LinkedList()
llist3.append(1)
llist3.append(1)
llist3.append(1)
llist3.append(1)
llist3.append(2)
llist3.append(2)
llist3.delete_node(1)
print(llist3.to_list()) # [2,2]





