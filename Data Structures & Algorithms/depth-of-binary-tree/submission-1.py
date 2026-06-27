# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [root]

        ldep = 0
        rdep = 0

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                ldep+=1
            if node.right:
                stack.append(node.right)
                rdep+=1
        return ldep+rdep


        