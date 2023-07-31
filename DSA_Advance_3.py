#Q1.Implement Binary tree

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

# Example usage
if __name__ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("Inorder Traversal: ")
    inorder_traversal(root)

#Q2.Find height of a given tree

class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("Height of the tree is: ", height(root))


#Q3.Perform Pre-order, Post-order, In-order traversal

class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("In-order Traversal: ", end='')
    inorder_traversal(root)
    print("\nPre-order Traversal: ", end='')
    preorder_traversal(root)
    print("\nPost-order Traversal: ", end='')
    postorder_traversal(root)

#Q4.Function to print all the leaves in a given binary tree

class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def print_leaves(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end=' ')
        print_leaves(root.left)
        print_leaves(root.right)

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("Leaves: ", end='')
    print_leaves(root)

#Q5.Implement BFS (Breath First Search) and DFS (Depth First Search)

class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def bfs(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        print(node.data, end=' ')

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def dfs(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) != 0:
        node = stack.pop()
        print(node.data, end=' ')

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("BFS: ", end='')
    bfs(root)

    print("\nDFS: ", end='')
    dfs(root)

#Q6.Find sum of all left leaves in a given Binary Tree


class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def is_leaf(node):
    return node.left is None and node.right is None

def sum_left_leaves(root):
    if root is None:
        return 0

    sum = 0
    if root.left is not None:
        if is_leaf(root.left):
            sum += root.left.data
        else:
            sum += sum_left_leaves(root.left)

    sum += sum_left_leaves(root.right)

    return sum

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("Sum of left leaves: ", sum_left_leaves(root))


#Q7.Find sum of all nodes of the given perfect binary tree

class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def perfect_tree_sum(root):
    if root is None:
        return 0

    height = 0
    node = root
    while node is not None:
        height += 1
        node = node.left

    return (2 ** height) - 1

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

#Q8.Count subtress that sum up to a given value x in a binary tree


class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def count_subtrees_with_sum_x(root, x):
    if root is None:
        return 0

    count = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)

            sum = node.data
            if sum == x:
                count += 1

            left = node.left
            right = node.right
            while left or right:
                if left:
                    sum += left.data
                    if sum == x:
                        count += 1
                    left = left.left or left.right

                if right:
                    sum += right.data
                    if sum == x:
                        count += 1
                    right = right.right or right.left

    return count

# Example usage
if _name_ == '_main_':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    x = int(input("Enter the value of x: "))
    print("Number of subtrees with sum x: ", count_subtrees_with_sum_x(root, x))


#Q9.Find maximum level sum in Binary Tree

from collections import deque

class Node:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    queue = deque([root])
    max_sum = float('-inf')
    level = 0

    while queue:
        level += 1
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

    return max_level

#Example:
# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

max_level = max_level_sum(root)
print(max_level)

#Q10.Print the nodes at odd levels of a tree

class Node:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_levels(root):
    if not root:
        return

    print_odd_levels_helper(root, 1)

def print_odd_levels_helper(node, level):
    if not node:
        return

    if level % 2 == 1:
        print(node.val)

    print_odd_levels_helper(node.left, level + 1)
    print_odd_levels_helper(node.right, level + 1)
    
#Example:
# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_odd_levels(root)

