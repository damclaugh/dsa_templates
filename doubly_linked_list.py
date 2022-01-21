

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
            
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    def insert_after_node(self, key, value):
        cur_node = self.head

        while cur_node:
            # head = key and head is only element in list
            if cur_node.next is None and cur_node.value == key:
                self.append(value)
                return
            # somewhere else in the list
            elif cur_node.value == key:
                new_node = Node(value)
                nxt = cur_node.next
                cur_node.next = new_node
                new_node.next = nxt
                new_node.prev = cur_node
                nxt.prev = new_node
            
            cur_node = cur_node.next

    def insert_before_node(self, key, value):
        cur_node = self.head

        while cur_node:
            # head = key and head is only element in list
            if cur_node.prev is None and cur_node.value == key:
                self.prepend(value)
                return

            elif cur_node.value == key:
                new_node = Node(value)
                prev = cur_node.prev
                prev.next = new_node
                cur_node.prev = new_node
                new_node.next = cur_node
                new_node.prev = prev

            cur_node = cur_node.next
    
    def delete(self, value):
        
        # deleted value is at the head
        while self.head and self.head.value == value:
            # head node is only node in list
            if self.head.next is None:
                self.head = None
                return
            
            # node after the head node
            else:
                self.head = self.head.next
                self.head.prev = None
        
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:   
                # node is in middle of list
                # A - B - C
                if cur_node.next:
                    # nxt = cur_node.next # points to C
                    # prev = cur_node.prev # points to A
                    # prev.next = nxt # points A to C over B
                    # nxt.prev = prev # point C back to A over B
                    # cur_node = nxt

                    prev = cur_node.prev
                    prev.next = cur_node.next
                    cur_node.next.prev = prev
                    cur_node = cur_node.next

                # node to be deleted is last node
                # C - D
                else:
                    prev = cur_node.prev # points to C
                    prev.next = None # points C over D to point to None
                    cur_node.prev = None # don't need prev pointing back b/c D is getting deleted
                    return
            else:
                cur_node = cur_node.next

    def to_list(self):
        out_list = []
        cur_node = self.head
        
        while cur_node:
            out_list.append(cur_node.value)
            cur_node = cur_node.next
        
        return out_list


dll = DoublyLinkedList()
dll.append(3)
dll.append(4)
dll.append(4)
dll.prepend(2)
dll.prepend(1)
dll.prepend(1)
print(dll.to_list()) # [1, 1, 2, 3, 4, 4]
dll.delete(1)
dll.delete(3)
dll.delete(4)
print(dll.to_list()) # [2]
dll.append(5)
print(dll.to_list()) # [2, 5]
dll.insert_after_node(2, 11)
print(dll.to_list()) # [2, 11, 5]
dll.insert_before_node(11, 9)
dll.insert_before_node(5, 1)
print(dll.to_list()) # [2, 9, 11, 1, 5]