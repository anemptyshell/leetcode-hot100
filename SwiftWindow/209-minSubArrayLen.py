from typing import List

# 滑动窗口
# 为了避免陷入暴力解体的怪圈，只用一个for循环，那么这个循环的索引，一定是表示 滑动窗口的终止位置。
## 长度最小的子数组
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        # 在 Python 里，float('inf') 用于表示正无穷大，与之对应的 float('-inf') 则表示负无穷大。
        min_len = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while(sum >= target):

                min_len = min(min_len, right-left+1)
                sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

target = 7
nums = [2, 3, 1, 2, 4, 3]
solution = Solution()
res = solution.minSubArrayLen(target, nums)
print(res)  




