# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(curr):
            if not curr: return

            dfs(curr.left)
            res.append(curr.val)
            dfs(curr.right)

        dfs(root)
        return res