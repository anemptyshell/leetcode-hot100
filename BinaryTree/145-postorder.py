from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)

        return res
        