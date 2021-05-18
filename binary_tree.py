

# each has at most 2 children

# DFS traversals (where does root go? pre, in, or post?)
# preorder: root -> left -> right
# inorder: left -> root -> right
# postorder: left -> right -> root

#           1
#         /   \
#        2     3
#       / \   / \ 
#      4   5 6   7

# preorder: 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7 
# inorder: 4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
# postorder: 4 -> 5 -> 2 -> 6 -> 7 -> 3 -> 1

# O(n) time complexity

# BFS traversal
# level order: [[1], [2, 3], [4, 5, 6, 7]]



class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = TreeNode(value) # create new node based on value
    
    def get_root(self):
        return self.root

    # root -> left -> right
    # recursive solution
    def preorder_rec(self, node):
        if node is None:
            return []

        return [node.value] + self.preorder_rec(node.left) + self.preorder_rec(node.right)

    # iterative solution
    def preorder(self, node):
        if node is None:
            return []

        stack = [node] 
        result = []
        
        # add right value to stack and then left 
        # then when you pop from the stack, you get the left first
        while stack != []:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
        return result

    # left -> root -> right
    # recursive solution
    def inorder_rec(self, node):
        if node is None:
            return []

        return self.inorder_rec(node.left) + [node.value] + self.inorder_rec(node.right)

    # iterative solution
    def inorder(self, node):
        if node is None:
            return []

        stack = []
        result = []

        while node is not None or stack != []:
            while node is not None:
                stack.append(node)
                node = node.left # go left
            node = stack.pop()
            result.append(node.value)
            node = node.right
        
        return result

    # left -> right -> root
    # recursive solution
    def postorder_rec(self, node):
        if node is None:
            return []

        return self.postorder_rec(node.left) + self.postorder_rec(node.right) + [node.value]

    # iterative solution
    def postorder(self, node):
        if node is None:
            return []

        stack = [node]
        result = []

        while stack != []:
            node = stack.pop()
            result.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result[::-1]


    # paths from root to leaves
    def tree_paths(self, node):
        if not node:
            return []

        paths = []
        stack = [(node, str(node.value))]
        
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.value)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.value)))
        
        return paths


    def bfs(self, node):
        queue = []
        visit_order = []
        queue.append(node)
        
        while(len(queue) > 0):
            node = queue.pop(0)
            # visit that node
            visit_order.append(node.value)
            # add left or right child if it exists
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return visit_order


    # iterative solution
    def max_depth(self, node):
        if node is None:
            return 0
        
        depth = 0
        q = []
        q.append(node)

        while q:
            depth += 1
            temp = []

            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right) 
            q = temp
        
        return depth

    # top down approach
    def max_depth_top(self, node):
        if node is None:
            return 0
        
        return (1 + max(self.max_depth_top(node.left), self.max_depth_top(node.right)))

    # bottom up approach
    def max_depth_bottom(self, node):
        if node is None:
            return 0
        else:
            left = self.max_depth_bottom(node.left)
            right = self.max_depth_bottom(node.right)
            
            return 1 + max(left, right)

    # size is number of nodes
    def size(self): 
        if self.root is None:
            return 0

        stack = []
        stack.append(self.root)
        size = 1
        while stack != []:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)
        
        return size



tree = BinaryTree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)
root = tree.get_root()
print(tree.preorder_rec(root)) # [1, 2, 4, 5, 3, 6, 7]
print(tree.preorder(root)) # [1, 2, 4, 5, 3, 6, 7]
print(tree.inorder(root)) # [4, 2, 5, 1, 6, 3, 7]
print(tree.inorder_rec(root)) # [4, 2, 5, 1, 6, 3, 7]
print(tree.postorder_rec(root)) # [4, 5, 2, 6, 7, 3, 1]
print(tree.postorder(root)) # [4, 5, 2, 6, 7, 3, 1]
print(tree.tree_paths(root)) # ['1->3->7', '1->3->6', '1->2->5', '1->2->4']
print(tree.bfs(root)) # [1, 2, 3, 4, 5, 6, 7]
print(tree.max_depth(root)) # 3
print(tree.max_depth_top(root)) # 3
print(tree.max_depth_bottom(root)) # 3
print(tree.size()) # 7

