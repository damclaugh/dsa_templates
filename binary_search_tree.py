
# BST implementation with insert, search, delete methods

# each node value must be > values stored in its left subtree
# each node value must be < values stored in its right subtree.

# inorder traversal (left -> root -> right) most frequent traversal method

# valid bst:
#           8
#         /   \ 
#        3     10
#       / \   /  \
#      1   6 9   11

# not valid bst
#           12
#         /    \
#       3       14 
#     /  \     /   \
#    1   13   11   15
# 13 is > 12 so shouldn't be in left tree (if 13 was 2 also not valid bst)

# search complexity is O(log n)
# insertion is O(log n) in average case, O(n) in worst case


import math

class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = TreeNode(value)

    def get_root(self):
        return self.root

    def build_tree(self, list):
        for i in list:
            self.insert(i)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        node = self.root
        # traverse down tree to find insertion point
        while node:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

        # insert value to the left if < parent
        # insert value to the right if > parent
        if value < parent.value:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)

    def insert_rec(self, value):
        # if tree is empty
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    # method for recursive insertion
    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def search(self, value):
        node = self.root

        while node is not None:
            if node.value == value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        
        return False

    def find_min(self):
        node = self.root
        
        # left-most node in tree is the minimum
        while node.left is not None:
            node = node.left
        
        return node.value

    def find_max(self):
        node = self.root

        # right-most node in tree is the maximum
        while node.right is not None:
            node = node.right
        
        return node.value
    
    # left -> root -> right
    # prints node value in increasing order
    def inorder_trav(self, node):
        if node is None:
            return []
        
        stack = []
        result = []

        while node is not None or stack != []:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.value)
            node = node.right
        
        return result

    def delete(self, root, value):
        node = root
        parent = None

        # search for node
        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        
        if node is None: # value not in tree
            return root

        # node found
        # deletion: 4 cases
        # 1) node is leaf node
        if node.left is None and node.right is None:
            new = None
        
        # 2) node has right child only
        elif node.left is None:
            new = node.right

        # 3) node has left child only
        elif node.right is None:
            new = node.left

        # 4) node has two children
        # make the right subtree the main branch
        # insert the former left branch at the left-most available position
        else:
            new = node.right
            n2 = new
            # find left-most side of node.right
            while n2.left is not None:
                n2 = n2.left
            # place node.left at the left-most position of the new subtree
            n2.left = node.left

        # insert new node from aboce to replace node to be deleted
        if parent is None: # root node deleted
            return new
        
        if parent.left == node:
            parent.left = new
        
        else:
            parent.right = new
        
        return root
 
    # validates with inorder traversal
    # if valid bst, list of nodes will be in increasing order
    def validate_bst_trav(self):
        stack = []
        result = []
        node = self.root
        
        while node is not None or stack != []:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if result != [] and node.value <= result[-1]:
                return False
            result.append(node.value)
            node = node.right
        
        return True



elements = [17, 4, 1, 20, 9, 23, 18, 34]
tree = Tree()
tree.build_tree(elements)
root = tree.get_root()
print(tree.validate_bst_trav()) # True
print(tree.inorder_trav(root))
print(tree.find_min()) # 1
print(tree.find_max()) # 34
print(tree.search(20)) # True
print(tree.search(34)) # True
tree.delete(root, 20)
print('Is 20 in tree?', tree.search(20)) # False

