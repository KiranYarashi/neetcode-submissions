# Definition for a binary tree currentNode.
# class TreecurrentNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreecurrentNode]) -> bool:
        
        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            # Left subtree values must be < node.val
            # Right subtree values must be > node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        # Initialize with negative and positive infinity bounds
        return dfs(root, float('-inf'), float('inf'))
            


             