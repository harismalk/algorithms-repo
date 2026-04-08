# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack:
            pair = stack.pop()

            t1, t2 = pair[0], pair[1]
            
            if not t1 and not t2:
                continue

            if not t1 or not t2 or (t1.val != t2.val):
                return False
            
            stack.append((t1.right, t2.right))
            stack.append((t1.left, t2.left))
        
        return True

            
        