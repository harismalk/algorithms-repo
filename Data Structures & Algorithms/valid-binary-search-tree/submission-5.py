# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low, high):
            if not node:
                return True
            if node.left and node.left.val >= low:
                return False
            if node.right and node.right.val <= high:
                return False
                
            low = min(low, node.val)
            high = max(high, node.val)
            dfs(node.left, low, high)
            dfs(node.right, low, high)
            return True
        return dfs(root, root.val, root.val)
            



               