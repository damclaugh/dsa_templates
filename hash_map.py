
# key -> hash -> bucket
# common hash function is hash = value % base
# base determines number of buckets
# trade-off between space and number of collisions
# insert, lookup and delete are O(1) time complexity on average; O(n) in worst case


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, initial_capacity=13):
        self.capacity = initial_capacity
        self.bucket = [None for item in range(self.capacity)]

    # converts string to index value
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.capacity
     
    # add key, value pair
    def add(self, key, value):
        index = self.get_hash(key)
        node = self.bucket[index]

        # if bucket is still empty from initialization
        # add key, value
        if node is None:
            self.bucket[index] = Node(key, value)
            return
        
        # otherwise there's a collision
        # iterate to end of linked list
        while node is not None:
            prev = node
            node = node.next

        # add node at end of list
        prev.next = Node(key, value)

    def find(self, key):
        index = self.get_hash(key)
        
        # go to first node and traverse linked list
        node = self.bucket[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None # not found
        else:
            return node.value

    def remove(self, key):
        index = self.get_hash(key)
        node = self.bucket[index]
        prev = None

        # iterate through bucket looking for requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next    

        # reach the end and key isn't there
        if node is None:
            return None

        # else key found
        else:
            result = node.value
            # delete node
            if prev is None:
                node = Node
            else:
                prev.next = prev.next.next

    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nHash map:"

        node = self.bucket
        for index, node in enumerate(self.bucket):
            if node is None:
                output += '\n[{}]'.format(index)
            else:
                output += '\n[{}]'.format(index)
                while node is not None:
                    output += ' ({}, {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
            
        return output


# TEST CASES
t = HashMap()
t.add('March 1', 127)
t.add('March 6', 130)
t.add('March 19', 173)
t.add('March 31', 142)
print(t.find('March 6')) # prints 130

print(t)
# prints: 
# Hash map:
# [0] (March 1, 127) 
# [1] 
# [2] 
# [3] 
# [4] 
# [5] (March 6, 130)  -->  (March 19, 173) 
# [6] 
# [7] 
# [8] 
# [9] 
# [10] 
# [11] 
# [12] (March 31, 142)