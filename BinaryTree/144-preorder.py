## 定义
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 前序遍历
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            ## 如果 node 为空，执行 return 语句，这会使函数立即返回，不再执行后续的代码。
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res

# 示例用法
# 构建一个简单的二叉树
#       1
#        \
#         2
#        /
#       3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
res = solution.preorderTraversal(root)
print(res) 