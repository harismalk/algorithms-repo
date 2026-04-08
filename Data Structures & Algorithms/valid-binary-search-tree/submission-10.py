# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(low, high, node):
            if not node:
                return True
            if low < node.val < high:
                left = dfs(low, node.val, node.left)
                right = dfs(node.val, high, node.right)
                return left and right
            else:
                return False
        return dfs(float("-INF"), float("INF"), root)
        