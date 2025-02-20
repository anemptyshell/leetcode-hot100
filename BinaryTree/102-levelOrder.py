from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 需要借用队列来实现，队列先进先出，符合一层一层遍历的逻辑，而用栈先进后出适合模拟深度优先遍历也就是递归的逻辑
## 从上到下、从左到右

## deque：类似于list的容器，可以快速的在队列头部和尾部添加、删除元素
## popleft()：移除列表中的一个元素（默认最左端的一个元素），并且返回该元素的值
## append()：从右端添加元素（与list同）

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ## 初始化队列
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            ## 当前层的节点数
            level_size = len(queue)
            curr_level = []

            for i in range(level_size):
                # 从队列中取出一个节点
                node = queue.popleft()
                # 访问节点的值
                curr_level.append(node.val)

                # 如果有左子节点，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果有右子节点，加入队列
                if node.right:
                    queue.append(node.right)
            
            result.append(curr_level)

        return result
        ## 注意return语句的缩进，在这里不能和上一句对齐


# 构建一个简单的二叉树
#       3
#      / \
#     9  20
#       /  \
#      15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 执行层序遍历
solution = Solution()
result = solution.levelOrder(root)
print(result)  # 输出: [[3], [9, 20], [15, 7]]


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                result.append(node.val)

                # 如果有左子节点，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果有右子节点，加入队列
                if node.right:
                    queue.append(node.right)
          
        return result
## 上述代码犯的错误：返回值类型是List[int]，而不是期望的List[List[int]]
## 例如正确答案是[[3],[9,20],[15,7]]，得到的却是[3,9,20,15,7]