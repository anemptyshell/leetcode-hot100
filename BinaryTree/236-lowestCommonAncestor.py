
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 所有节点的值都是唯一的。
## p、q 为不同节点且均存在于给定的二叉树中。
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
              
        def dfs(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            # 递归遍历左子树
            left = dfs(node.left, p, q)
            # 递归遍历右子树
            right = dfs(node.right, p, q)

            # 如果左右子树都返回了非空节点，说明 p 和 q 分别在左右子树中，当前节点就是最近公共祖先
            if left and right:
                return node
            # 如果左子树返回非空节点，右子树为空，说明 p 和 q 都在左子树中，返回左子树的结果
            elif left is not None and right is None: 
                return left
            # 如果右子树返回非空节点，左子树为空，说明 p 和 q 都在右子树中，返回右子树的结果
            elif right is not None and left is None: 
                return right
            # 如果左右子树都为空，返回 None
            else:
                return None
        
        res = dfs(root, p, q)
        return res

# 我们可以采用深度优先搜索（DFS）的策略，从根节点开始递归遍历二叉树。对于每个节点，有以下几种情况：

# 节点为空：如果当前节点为空，直接返回 None。
# 节点等于 p 或 q：如果当前节点等于 p 或者 q，说明找到了其中一个目标节点，返回该节点。

# 递归遍历左右子树：分别递归遍历当前节点的左子树和右子树，得到左右子树的返回结果 left 和 right。
# 左右子树都不为空：说明 p 和 q 分别位于当前节点的左右子树中，那么当前节点就是它们的最近公共祖先，返回当前节点。
# 左子树不为空，右子树为空：说明 p 和 q 都在左子树中，返回左子树的返回结果 left。
# 右子树不为空，左子树为空：说明 p 和 q 都在右子树中，返回右子树的返回结果 right。
# 左右子树都为空：说明 p 和 q 都不在当前节点的子树中，返回 None。       

## 代码随想录
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == q or root == p or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left
        else: 
            return None