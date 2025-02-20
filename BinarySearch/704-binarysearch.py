class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        
        while(i <= j):
            # m = (i + j) // 2
            # 优化中间位置的计算，避免整数溢出
            m = i + (j - i) // 2
            if(target < nums[m]):
                j = m - 1
            elif(target > nums[m]):
                i = m + 1
            else:
                return m
               
        return -1

# 首先计算 j - i，也就是当前搜索区间的长度。由于 j 和 i 分别是搜索区间的结束位置和起始位置，且 j >= i，
# 所以 j - i 的结果不会超出整数类型的表示范围。
# 然后将 j - i 的结果除以 2，得到从起始位置 i 到中间位置的偏移量。
# 最后把这个偏移量加到起始位置 i 上，就得到了中间位置 m。


nums = [1, 2, 3, 4, 5]
target = 6
solution = Solution()
result = solution.search(nums, target)
print(result)