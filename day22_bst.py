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
        # initialize leftNode to zero
        leftNode = 0
        # initialize rightNode to zero
        rightNode = 0
        # check if root.left is not None
        if root.left is not None:
            # increment leftNode by 1 and sum the recursive call to getHeight
            leftNode = 1 + self.getHeight(root.left)
        # check if root.right is not None
        if root.right is not None:
            # increment rightNode by 1 and sum the recursive call to getHeight
            rightNode = 1 + self.getHeight(root.right)
        # return the max of max of leftNode and rightNode
        return max(leftNode, rightNode)

        # print(root.data)
        # if root.left is not None:
        #     # call getHeight on it passing it left
        #     self.getHeight(root.left)
        # # if the popped right is not None
        # if root.right is not None:
        #     # call getHeight on it passing it right
        #     self.getHeight(root.right)


myTree = Solution()
root = None

nodes = [3, 5, 2, 1, 4, 6, 7]

for node in nodes:
    root = myTree.insert(root, node)

print(myTree.getHeight(root))
