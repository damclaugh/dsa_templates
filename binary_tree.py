

# each has at most 2 children

# DFS traversals (where does root go? pre, in, or post?)
# preorder: root -> left -> right (visit node before its children)
# inorder: left -> root -> right
# postorder: left -> right -> root (visit node after the children)

#           1
#         /   \
#        2     3
#       / \   / \ 
#      4   5 6   7

# preorder: 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7 
# inorder: 4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
# postorder: 4 -> 5 -> 2 -> 6 -> 7 -> 3 -> 1

# traversals are O(n) time complexity

# BFS traversal
# level order: [[1], [2, 3], [4, 5, 6, 7]]


from collections import deque

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

    # root -> left -> right
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

    # left -> root -> right
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
            node = stack.pop() # gets left most leaf
            result.append(node.value)
            node = node.right
        
        return result

    # left -> right -> root
    # recursive solution
    def postorder_rec(self, node):
        if node is None:
            return []

        return self.postorder_rec(node.left) + self.postorder_rec(node.right) + [node.value]

    # left -> right -> root
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


    # breadth-first search
    def bfs(self, node):
        
        queue = [node]
        result = []
        
        while queue != []:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

        # # # separate lists for each level
        # queue = [node]  
        # result = []
        # while queue != []:
        #     level = []
        #     next_queue = []
        #     for node in queue:
        #         level.append(node.value)
        #         if node.left:
        #             next_queue.append(node.left)
        #         if node.right:
        #             next_queue.append(node.right)
        #     result.append(level)
        #     queue = next_queue
                
        # return result

    
    # leaf nodes
    def leaves(self, node):

        stack = [node]
        result = []

        while stack != []:
            node = stack.pop()
            if node.left is None and node.right is None:
                result.append(node.value)
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return result

    
    # paths from root to leaves
    def tree_paths(self, node):
        if not node:
            return []

        paths = []
        stack = [(node, [node.value])]
        
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + [node.left.value]))
            if node.right:
                stack.append((node.right, path + [node.right.value]))
        
        return paths

        ## With arrow formatting ##
        # if not node:
        #     return []

        # paths = []
        # stack = [(node, str(node.value))]
        
        # while stack:
        #     node, path = stack.pop()
        #     if not node.left and not node.right:
        #         paths.append(path)
        #     if node.left:
        #         stack.append((node.left, path + '->' + str(node.left.value)))
        #     if node.right:
        #         stack.append((node.right, path + '->' + str(node.right.value)))
        
        # return paths


    # sums of root-to-leaf paths
    def path_sums(self, node):
        if not node:
            return []

        path_sums = []
        stack = [(node, node.value)]
        
        while stack:
            node, path_sum = stack.pop()
            if not node.left and not node.right:
                path_sums.append(path_sum)
            if node.left:
                stack.append((node.left, path_sum + node.left.value))
            if node.right:
                stack.append((node.right, path_sum + node.right.value))
        
        return path_sums

    def height_rec(self, node):
        if node is None:
            return 0 # change to -1 if node itself is considered level 0
        
        left_height = self.height_rec(node.left)
        right_height = self.height_rec(node.right)

        return 1 + max(left_height, right_height)

    # return number of nodes
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

    # check height of left subtree and right subtree of every node
    # if diff > 1, not balanced
    def is_balanced(self, node):

        queue = [node]
        height = 0
        
        while queue != []:
            node = queue.pop(0)
            
            if node.left:
                left_height = self.depth(node.left)
                queue.append(node.left)
            else:
                left_height = 0
            if node.right:
                right_height = self.depth(node.right)
                queue.append(node.right)
            else:
                right_height = 0

            if abs(left_height-right_height) > 1:
                return False
        
        return True

    def depth(self, node):

        depth = 0
        stack = [node]

        while stack != []:
            depth += 1
            level = []
            for node in stack: 
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            stack = level
        
        return depth

    def zigzag_trav(self, node):
        # do regular bfs
        # if even numbered level, reverse order of nodes added to result
        
        queue = [node]  
        result = []
        level_count = 0
        
        while queue != []:
            level_count += 1
            level = []
            next_queue = []
            for node in queue:
                level.append(node.value)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if level_count % 2 == 0:
                result.append(level[::-1])
            else:
                result.append(level)
            queue = next_queue
                
        return result

    def vertical_trav(self, node):

        # use hash table where node values are grouped by column index
        # values in the list should be ordered by their rows
        col_dict = {}
        queue = deque([(node, 0)])

        while queue:
            node, column = queue.popleft()

            if column not in col_dict:
                col_dict[column] = [node.value]
            else:
                col_dict[column].append(node.value)
            
            if node.left:
                queue.append((node.left, column-1))
            if node.right:
                queue.append((node.right, column+1))

        result = []
        for k, v in sorted(col_dict.items()):
            result.append(v)

        return result

    def invert(self, root):

        stack = [root]
        
        while stack != []:          
            level = []
            for node in stack:
                temp = node.left
                node.left = node.right
                node.right = temp
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            stack = level


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
print(tree.path_sums(root)) # [11, 10, 8, 7]
print(tree.bfs(root)) # [1, 2, 3, 4, 5, 6, 7]
print(tree.height_rec(root)) # 3
print(tree.depth(root)) # 3
print(tree.size()) # 7

tree = BinaryTree(7)
tree.root.right = TreeNode(6)
tree.root.right.left = TreeNode(3)
tree.root.right.right = TreeNode(5)
tree.root.right.right.left = TreeNode(2)
tree.root.right.right.right = TreeNode(4)
root = tree.get_root()
print(tree.is_balanced(root))
print(tree.depth(root))
print(tree.height_rec(root))


