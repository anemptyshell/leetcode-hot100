from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dict:
                res.append(dict[target - nums[i]])
                res.append(i)
            
            dict[nums[i]] = i
        
        return res

## 使用哈希表（字典）来存储元素及其索引,将查找目标元素的时间复杂度从暴力解法的 O(n^2) 降低到了O(n) 
# 因为字典的查找操作平均时间复杂度为 O(1)。
"""改进：找到满足条件的两个数后立即返回结果，这样可以避免不必要的遍历"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]        
            
            dict[nums[i]] = i
        
        return []