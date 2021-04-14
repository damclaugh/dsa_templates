
# BST implementation with insert, search, delete methods

# Each node value must be > values stored in its left subtree
# Each node value must be < values stored in its right subtree.

# Inorder traversal (left -> root -> right) most frequent traversal method

# valid bst:
#           8
#         /   \ 
#       3       10
#     /   \    /  \
#    1     6  9    11

# not valid bst
#           12
#         /    \
#       3       14 
#     /  \     /   \
#    1   13   11   15
# 13 is > 12 so shouldn't be in left tree (if 13 was 2 also not valid bst)

# Insertion is O(log n) in average case, O(n) in worst case


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
        else:
            self._insert(self.root, value)

    # method for iterative insertion
    def _insert(self, root, value):
        node = root

        # traverse down tree to find insertion point
        while node:
            parent = node

            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right

        # insert value to the left if < parent
        # insert value to the right if > parent
        if value < parent.value:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)

        return root

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

        return

    def search(self, value):
        node = self.root
        if node.value == value:
            return True
        
        # traverse down tree looking for value
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def search_rec(self, value):
        if self.root:
            found = self._search_rec(self.root, value)
            if found:
                return True
            else:
                return False
        else:
            return None

    # method for recursive search
    def _search_rec(self, node, value):
        if value > node.value and node.right:
            return self._search_rec(node.right, value)

        elif value < node.value and node.left:
            return self._search_rec(node.left, value)
        
        if value == node.value:
            return True

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

    def print_tree(self):
        return self.inorder_trav(self.root, "")
        
    def inorder_trav(self, root, trav):
        # left -> right -> root
        if root is None:
            return

        if root.left:
            trav = self.inorder_trav(root.left, trav)
        trav += (str(root.value) + '->')
        if root.right:
            trav = self.inorder_trav(root.right, trav)

        return trav

    def delete(self, value):
        return self._delete(self.root, value)
    
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.value

    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.value
    
    # solution from https://leetcode.com/problems/delete-node-in-a-bst/solution/
    def _delete(self, node, value):
        if not node:
            return None

        if value > node.value:
            node.right = self._delete(node.right, value)

        elif value < node.value:
            node.left = self._delete(node.left, value)
        
        # delete current node
        else:
            # node is a leaf
            if not (node.left or node.right):
                node = None
            # node is not a leaf and has right child (could have left and right child)
            # replace node with successor
            # then delete successor
            elif node.right:
                node.value = self.successor(node)
                node.right = self._delete(node.right, node.value)
            # node is not a leaf, has no right child, and has left child
            # replace node with predecessor
            # delete predecessor
            else:
                node.value = self.predecessor(node)
                node.left = self._delete(node.left, node.value)

        return node

# checks if tree is a valid BST
def validate_bst(root, min = -math.inf, max = math.inf):
    if root is None:
        return True

    if (root.value > min and 
        root.value < max and
        validate_bst(root.left, min, root.value) and
        validate_bst(root.right, root.value, max)):
        return True
    else:
        return False

# another function to check if tree is a valid BST
def validate_bst2(root):
    def check(root, l, r):
        if root is None:
            return True
        value = root.value
        if value <= l or value >= r:
            return False
        return check(root.left, l, value) and check(root.right, value, r)
    return check(root, -math.inf, math.inf)

# validates with inorder traversal
# if valid bst, list of nodes will be in increasing order
def validate_bst_trav(root):
    q = []
    def inorder_dfs(node):
        if node is None:
            return True
        inorder_dfs(node.left)
        q.append(node.value)
        inorder_dfs(node.right)
    inorder_dfs(root)

    for i in range(len(q)-1):
        if q[i] > q[i+1]:
            return False
    return True


# TEST CASES
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.right.left = TreeNode(8)
root.right.right = TreeNode(15)
print('Valid BST?', validate_bst(root)) # prints True
print('Valid BST?', validate_bst_trav(root)) # prints True


elements = [17, 4, 1, 20, 9, 23, 18, 34]
tree = Tree()
tree.build_tree(elements)
print('Valid BST?', validate_bst_trav(tree.root)) # prints True
print('Tree nodes: ', tree.print_tree()) # prints 1->4->9->17->18->20->23->34->
print('Minimum value: ', tree.find_min()) # prints 1
print('Is 20 in tree?', tree.search(20)) # prints True
print('Is 34 in tree?', tree.search_rec(34)) # prints True
print('Deleting 20')
tree.delete(20)
print('Is 20 in tree?', tree.search(20)) # prints False

