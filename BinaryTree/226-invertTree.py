from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def helper(node):
            left = node.left
            right = node.right

            node.left = right
            node.right = left

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            ## 以下递归终止条件冗余
            # if not node.left and not node.right:
            #     return
     
        helper(root)
        return root
        ## 注意函数的返回值是什么，不要忘记！

# 构建一个简单的二叉树
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
inverted_root = solution.invertTree(root)

# 简单的前序遍历函数，用于验证翻转结果
def preorder_traversal(node):
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("翻转后的二叉树前序遍历结果:")
preorder_traversal(inverted_root)