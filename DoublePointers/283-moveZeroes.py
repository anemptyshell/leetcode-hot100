from typing import List

## 移动0
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:

        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        
        return nums
        
## 使用两个指针，一个指针 slow 用于标记非零元素应该存放的位置，另一个指针 fast 用于遍历数组。
# 遍历过程中，当 fast 指针指向的元素不为 0 时，将该元素与 slow 指针指向的位置进行交换，
# 然后 slow 指针向后移动一位。最后，将 slow 指针之后的所有位置都置为 0。

