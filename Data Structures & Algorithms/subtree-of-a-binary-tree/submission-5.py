# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return True
        if subRoot and not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or (self.isSubtree(root.right, subRoot))

            
        
    def sameTree(self, n1, n2):
        if not n1 and not n2:
            return True
        if (n1 and not n2) or (n2 and not n1) or (n1.val != n2.val):
            return False
        left = self.sameTree(n1.left, n2.left)
        right = self.sameTree(n1.right, n2.right)
        return right and left
        