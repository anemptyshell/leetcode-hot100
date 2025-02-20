from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
           
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1                
                    left += 1
                    right -= 1          
        return res

## break 语句用于立即终止当前所在的循环，跳出循环体，不再执行循环中剩余的代码，也不会再进行后续的循环迭代。
## continue 语句用于跳过当前循环中剩余的代码，直接进入下一次循环的迭代。

# 1.排序数组：首先对数组 nums 进行排序，这样相同的元素会相邻排列，方便后续去重操作，同时也便于使用双指针法。
# 2.遍历数组并固定一个元素：遍历排序后的数组，将当前元素作为三元组的第一个元素 nums[i]。
# 3.使用双指针寻找另外两个元素：对于每个固定的 nums[i]，在其右侧使用双指针 left 和 right 分别指向 i + 1 和数组末尾。
# 计算 nums[i] + nums[left] + nums[right] 的和 sum，根据 sum 的值调整指针：
#     如果 sum 等于 0，则找到了一个满足条件的三元组，将其添加到结果列表中，并移动 left 和 right 指针，同时跳过重复元素。
#     如果 sum 小于 0，说明需要增大和，将 left 指针右移。
#     如果 sum 大于 0，说明需要减小和，将 right 指针左移。
# 4.去重处理：在遍历过程中，需要跳过重复的元素，避免结果中出现重复的三元组。