
## 和为k的子数组
from typing import List

## 时间复杂度O(n)，其中 n 是数组 nums 的长度。因为只需要对数组进行一次遍历，每次操作哈希表的时间复杂度为O(1) 
## 空间复杂度O(n)，在最坏情况下，哈希表可能需要存储 n 个不同的前缀和。
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        res = 0
        current_sum  = 0

        for i in range(len(nums)):

            current_sum  += nums[i]
            if current_sum -k in prefix_sum:
                # res += 1 
                # ## 这行代码只简单地将结果 res 加 1，但没有考虑到 sum - k 在前缀和哈希表中可能出现多次的情况。
                res += prefix_sum[current_sum  - k]

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return res

solution = Solution()
nums = [2,1,0,1,1,3]
k = 3
print(solution.subarraySum(nums, k))  # 输出应该为 4     


