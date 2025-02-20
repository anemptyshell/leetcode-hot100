## 无重复字符的最长子串

## 时间复杂度 n
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        hash_map = {}
        left = 0
        for right in range(len(s)):

            # 如果当前字符已经在哈希表中，并且其上次出现的位置在左指针右侧
            if s[right] in hash_map and hash_map[s[right]] >= left:
                left = hash_map[s[right]] + 1

            hash_map[s[right]] = right
            swift_window = right - left + 1
            max_length = max(swift_window, max_length)
        
        return max_length

            
"abcdcabdac"




## 时间复杂度n^2，因为有两层嵌套循环
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         max_length = 0
#         for left in range(len(s)):
#             right = left
#             hash_map = {}
#             while right < len(s):
#                 if s[right] in hash_map:
#                     max_length = max(max_length, right - left)
#                     # continue
#                     break
#                 hash_map[s[right]] = right
#                 right += 1
#             max_length = max(max_length, right - left)

#         return max_length

