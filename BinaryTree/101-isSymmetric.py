from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(n1, n2):
            
            # 如果两个节点都为空，说明对称
            if not n1 and not n2:
                return True
            # 如果其中一个节点为空，另一个不为空，说明不对称
            if not n1 or not n2:
                return False
            ## 如果 n1 和 n2 都为 None，就会进入 if not n1 and not n2: 这个条件分支
            ## 直接返回 True，而不会执行到 if not n1 or not n2: 这里。

            # 比较当前两个节点的值，如果不相等则不对称
            if n1.val != n2.val:
                return False

            res1 = isMirror(n1.left, n2.right)
            res2 = isMirror(n1.right, n2.left)

            return res1 and res2
        
        return isMirror(root, root)


