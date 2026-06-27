# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        r, l = 1, 1
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                r +=1
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                l+=1
        return abs(r-l) <=1
            




        