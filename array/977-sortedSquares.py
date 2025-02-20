from typing import List

# 那么数组平方的最大值就在数组的两端，不是最左边就是最右边，不可能是中间。
# 此时可以考虑双指针法了，i指向起始位置，j指向终止位置。

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        # num: List[int] = [] 
        # 上面这行代码的问题：num 初始化为空列表 []，但后续代码直接使用 num[k] 来赋值，由于空列表没有索引为 k 的元素
        # 会导致 IndexError 异常。（超出索引范围）

        # 预先创建一个和输入数组长度相同的结果数组
        num = [0] * len(nums)
        k = len(nums)-1

        while i<=j:
            if nums[i] * nums[i] <= nums[j] * nums[j]:
                num[k] = nums[j] * nums[j]
                k -= 1
                j -= 1

            elif nums[i] * nums[i] > nums[j] * nums[j]:
                num[k] = nums[i] * nums[i]
                k -= 1
                i += 1
        
        return num


solution = Solution()
nums = [-4, -1, 0, 3, 10]
result = solution.sortedSquares(nums)
print(result)
