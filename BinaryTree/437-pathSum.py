from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 前缀和的概念：前缀和是指从根节点到当前节点路径上所有节点值的累加和。我们可以使用一个哈希表来记录每个前缀和出现的次数。
"""时间复杂度为 n"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        result = 0
        prefix_sum = {0:1}

        def dfs(node, curr_sum):
            if not node:
                return
            nonlocal result

            # 计算当前节点的前缀和
            curr_sum += node.val

            # 检查是否存在路径和等于 targetSum
            if curr_sum - targetSum in prefix_sum:
                result += prefix_sum[curr_sum - targetSum]
            
            # 更新前缀和的计数
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # 回溯操作，将当前节点的前缀和计数减 1
            prefix_sum[curr_sum] -= 1
        
        dfs(root, 0)
        return result
      

    



"""时间复杂度为n^2"""
# class Solution:

#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

#         path_num = 0

#         def dfs(node, sum):
#             nonlocal path_num           
#             if not node:
#                 return
#             sum -= node.val
#             if sum == 0:
#                 path_num += 1
#             if not node.left and not node.right:
#                 return         
#             dfs(node.left, sum)
#             dfs(node.right, sum)

#         def dfs2(node):
#             if not node:
#                 return
#             dfs(node, targetSum)
#             dfs2(node.left)
#             dfs2(node.right)

#         dfs2(root)
#         return path_num
    


      
        
            
