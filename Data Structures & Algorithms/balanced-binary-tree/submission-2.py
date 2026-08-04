# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkHeight(root):

            if not root:
                return 0
            
            leftTreeHeight = checkHeight(root.left)
            if leftTreeHeight == -1:
                return -1

            rightTreeHeight = checkHeight(root.right)
            if rightTreeHeight == -1:
                return -1

            if abs(leftTreeHeight -rightTreeHeight ) > 1:
                return -1

            return 1 + max(leftTreeHeight , rightTreeHeight)

        result = checkHeight(root)

        if result == -1:
            return False
        else:
            return True
            

            



