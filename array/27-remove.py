from typing import List

# 定义两个指针，一个指针 i 用于遍历列表，
# 另一个指针 k 用于记录不等于 val 的元素应该存放的位置。
# 当遍历到的元素不等于 val 时，将该元素放到 k 所指向的位置，然后 k 指针向后移动一位。
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


    
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
result = solution.removeElement(nums, val)
print(result)