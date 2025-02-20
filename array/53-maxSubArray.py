
## 最大子数组和

## 动态规划问题，使用Kadane算法
## 时间O(n), 空间O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int :

        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
max = solution.maxSubArray(nums)
print(max) 


