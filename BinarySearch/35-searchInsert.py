from typing import List

## 时间 O(log n) ,空间 O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int :

        left = 0
        right = len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2    ## 注意：//才是整除，/不是
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m
        
        return left
            






