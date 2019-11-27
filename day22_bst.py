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
        # initialize leftNodes to zero
        leftNodes = 0
        # initialize rightNodes to zero
        rightNodes = 0
        # check if root.left is not None
        if root.left is not None:
            # increment leftNodes by 1 and sum the recursive call to getHeight
            leftNodes = 1 + self.getHeight(root.left)
        # check if root.right is not None
        if root.right is not None:
            # increment rightNodes by 1 and sum the recursive call to getHeight
            rightNodes = 1 + self.getHeight(root.right)
        # return the max of max of leftNodes and rightNodes
        return max(leftNodes, rightNodes)


myTree = Solution()
root = None

nodes = [3, 5, 2, 1, 4, 6, 7]

for node in nodes:
    root = myTree.insert(root, node)

print(myTree.getHeight(root))
