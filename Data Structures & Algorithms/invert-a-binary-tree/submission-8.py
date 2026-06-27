# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.right and node.left:
                node.right, node.left = node.left, node.right
            
            stack.append(node.right)
            stack.append(node.left)
        return root

