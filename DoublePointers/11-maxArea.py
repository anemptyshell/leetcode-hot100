from typing import List

## 时间O(n) 空间O(1)
## 盛最多水的容器
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
          
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            ## 错误！！！让两个指针同时向中间靠拢，无法根据两条垂线的长短情况做出正确的指针移动决策。
            # left += 1
            # right -= 1

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
max = solution.maxArea(height)
print(max)             
