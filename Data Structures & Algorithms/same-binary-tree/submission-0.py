# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):

            if root1 != root2:
                return False
            

            left1, left2 = root1.left, root2.left
            right1, right2 = root1.right, root2.right
            
            dfs(left1, left2)
            dfs(left1, left2)

            return True
    
        return dfs(p,q)



        

        