from typing import List


# 从列表创建集合
# my_list = [1, 2, 3, 3, 4]
# my_set = set(my_list)
# print(my_set)  # 输出：{1, 2, 3, 4}

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## 构建哈希表

        hash_nums = set(nums)
        longest_length = 0

        for num in hash_nums:

            if num - 1 not in hash_nums:
                curr_num = num
                curr_length = 1

                while curr_num + 1 in hash_nums:
                    curr_length += 1
                    curr_num += 1

                longest_length  = max(longest_length, curr_length)

        return longest_length
     


        