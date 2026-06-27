# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res

            if not node:
                return res
            dfs(node.left)
            cnt-=1
            if cnt == k:
                return node.val
            dfs(node.right)

        return dfs(root)
            

        
        