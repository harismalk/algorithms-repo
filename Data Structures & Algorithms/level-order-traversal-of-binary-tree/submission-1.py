# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        print(len(res))

        stack = [(root, 0)]

        while stack:
            curr, h = stack.pop()
            if h > len(res)-1:
                res.append([])
            res[h].append(curr.val)

            if curr.right:
                stack.append((curr.right, h+1))
            if curr.left:
                stack.append((curr.left, h+1))
        return res
                