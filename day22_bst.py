class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        # initialize stack to empty list
        stack = []
        # push the root to the stack
        stack.append(root)
        # loop while stack is not empty
        while len(stack) > 0:
            # pop the stack
            node = stack.pop()
            # if the popped left is not None
            if node.left is not None:
                # call getHeight on it passing it left
                self.getHeight(node.left)
            # if the popped right is not None
            if node.right is not None:
                # call getHeight on it passing it right
                self.getHeight(node.right)
