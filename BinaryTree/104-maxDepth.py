from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## 若根节点为空，树的深度为 0
        if not root:
            return 0
        ## 当输入的二叉树为空时，代码会将 None 加入队列，接着在后续处理中尝试访问 None 的属性，从而导致错误。

        queue = deque()
        queue.append(root)
        ## 代码在初始化队列时直接将 root 加入队列，却没有对 root 是否为空进行检查。
        ## 若 root 为空，后续访问 node.val 就会引发 AttributeError 异常。
        depth = 0

        while queue:
            depth += 1

            for i in range(len(queue)):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth


        


