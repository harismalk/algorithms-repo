# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #res = 0

        def dfs(node, curr_max):
            if not node:
                return 0

            if node.val >= curr_max:
                res = 1
            else:
                res = 0

            curr_max = max(curr_max, node.val)

            res += dfs(node.right, curr_max)
            res += dfs(node.left, curr_max)
            return res

        return dfs(root, 0)



        